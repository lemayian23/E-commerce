/** @ecommerce-module */

import { getecommerceFunctions } from "../helpers/ecommerce_functions_helpers";

/**
 * Parse a spreadsheet formula and detect the number of LIST functions that are
 * present in the given formula.
 *
 * @param {string} formula
 *
 * @returns {number}
 */
export function getNumberOfListFormulas(formula) {
    return getecommerceFunctions(formula, ["ecommerce.LIST", "ecommerce.LIST.HEADER"]).filter((fn) => fn.isMatched)
        .length;
}

/**
 * Get the first List function description of the given formula.
 *
 * @param {string} formula
 *
 * @returns {import("../helpers/ecommerce_functions_helpers").ecommerceFunctionDescription|undefined}
 */
export function getFirstListFunction(formula) {
    return getecommerceFunctions(formula, ["ecommerce.LIST", "ecommerce.LIST.HEADER"]).find((fn) => fn.isMatched);
}
