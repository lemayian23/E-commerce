/** @ecommerce-module **/

import spreadsheet from "../o_spreadsheet/o_spreadsheet_extended";

const { parse } = spreadsheet;

/**
 * @typedef {Object} ecommerceFunctionDescription
 * @property {string} functionName Name of the function
 * @property {Array<string>} args Arguments of the function
 * @property {boolean} isMatched True if the function is matched by the matcher function
 */

/**
 * This function is used to search for the functions which match the given matcher
 * from the given formula
 *
 * @param {string} formula
 * @param {string[]} functionNames e.g. ["ecommerce.LIST", "ecommerce.LIST.HEADER"]
 * @private
 * @returns {Array<ecommerceFunctionDescription>}
 */
export function getecommerceFunctions(formula, functionNames) {
    const formulaUpperCased = formula.toUpperCase();
    // Parsing is an expensive operation, so we first check if the
    // formula contains one of the function names
    if (!functionNames.some((fn) => formulaUpperCased.includes(fn.toUpperCase()))) {
        return [];
    }
    let ast;
    try {
        ast = parse(formula);
    } catch (_) {
        return [];
    }
    return _getecommerceFunctionsFromAST(ast, functionNames);
}

/**
 * This function is used to search for the functions which match the given matcher
 * from the given AST
 *
 * @param {Object} ast (see o-spreadsheet)
 * @param {string[]} functionNames e.g. ["ecommerce.LIST", "ecommerce.LIST.HEADER"]
 *
 * @private
 * @returns {Array<ecommerceFunctionDescription>}
 */
function _getecommerceFunctionsFromAST(ast, functionNames) {
    switch (ast.type) {
        case "UNARY_OPERATION":
            return _getecommerceFunctionsFromAST(ast.operand, functionNames);
        case "BIN_OPERATION": {
            return _getecommerceFunctionsFromAST(ast.left, functionNames).concat(
                _getecommerceFunctionsFromAST(ast.right, functionNames)
            );
        }
        case "FUNCALL": {
            const functionName = ast.value.toUpperCase();

            if (functionNames.includes(functionName)) {
                return [{ functionName, args: ast.args, isMatched: true }];
            } else {
                return ast.args.map((arg) => _getecommerceFunctionsFromAST(arg, functionNames)).flat();
            }
        }
        default:
            return [];
    }
}
