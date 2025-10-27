/** @ecommerce-module **/
import { getecommerceFunctions } from "@spreadsheet/helpers/ecommerce_functions_helpers";

/** @typedef  {import("@spreadsheet/helpers/ecommerce_functions_helpers").ecommerceFunctionDescription} ecommerceFunctionDescription*/

/**
 * @param {string} formula
 * @returns {number}
 */
export function getNumberOfAccountFormulas(formula) {
    return getecommerceFunctions(formula, ["ecommerce.BALANCE", "ecommerce.CREDIT", "ecommerce.DEBIT"]).filter(
        (fn) => fn.isMatched
    ).length;
}

/**
 * Get the first Account function description of the given formula.
 *
 * @param {string} formula
 * @returns {ecommerceFunctionDescription | undefined}
 */
export function getFirstAccountFunction(formula) {
    return getecommerceFunctions(formula, ["ecommerce.BALANCE", "ecommerce.CREDIT", "ecommerce.DEBIT"]).find(
        (fn) => fn.isMatched
    );
}
