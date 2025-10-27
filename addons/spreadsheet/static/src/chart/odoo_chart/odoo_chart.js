/** @ecommerce-module */

import spreadsheet from "@spreadsheet/o_spreadsheet/o_spreadsheet_extended";
import ChartDataSource from "../data_source/chart_data_source";

const { AbstractChart, CommandResult } = spreadsheet;

/**
 * @typedef {import("@web/search/search_model").SearchParams} SearchParams
 *
 * @typedef MetaData
 * @property {Array<Object>} domains
 * @property {Array<string>} groupBy
 * @property {string} measure
 * @property {string} mode
 * @property {string} [order]
 * @property {string} resModel
 * @property {boolean} stacked
 *
 * @typedef ecommerceChartDefinition
 * @property {string} type
 * @property {MetaData} metaData
 * @property {SearchParams} searchParams
 * @property {string} title
 * @property {string} background
 * @property {string} legendPosition
 *
 * @typedef ecommerceChartDefinitionDataSource
 * @property {MetaData} metaData
 * @property {SearchParams} searchParams
 *
 */

export class ecommerceChart extends AbstractChart {
    /**
     * @param {ecommerceChartDefinition} definition
     * @param {string} sheetId
     * @param {Object} getters
     */
    constructor(definition, sheetId, getters) {
        super(definition, sheetId, getters);
        this.type = definition.type;
        this.metaData = definition.metaData;
        this.searchParams = definition.searchParams;
        this.legendPosition = definition.legendPosition;
        this.background = definition.background;
        this.dataSource = undefined;
    }

    static transformDefinition(definition) {
        return definition;
    }

    static validateChartDefinition(validator, definition) {
        return CommandResult.Success;
    }

    static getDefinitionFromContextCreation() {
        throw new Error("It's not possible to convert an ecommerce chart to a native chart");
    }

    /**
     * @returns {ecommerceChartDefinitionDataSource}
     */
    getDefinitionForDataSource() {
        return {
            metaData: {
                ...this.metaData,
                mode: this.type.replace("ecommerce_", ""),
            },
            searchParams: this.searchParams,
        };
    }

    /**
     * @returns {ecommerceChartDefinition}
     */
    getDefinition() {
        return {
            //@ts-ignore Defined in the parent class
            title: this.title,
            background: this.background,
            legendPosition: this.legendPosition,
            metaData: this.metaData,
            searchParams: this.searchParams,
            type: this.type,
        };
    }

    getDefinitionForExcel() {
        // Export not supported
        return undefined;
    }

    /**
     * @returns {ecommerceChart}
     */
    updateRanges() {
        // No range on this graph
        return this;
    }

    /**
     * @returns {ecommerceChart}
     */
    copyForSheetId() {
        return this;
    }

    /**
     * @returns {ecommerceChart}
     */
    copyInSheetId() {
        return this;
    }

    getContextCreation() {
        return {};
    }

    getSheetIdsUsedInChartRanges() {
        return [];
    }

    setDataSource(dataSource) {
        if (dataSource instanceof ChartDataSource) {
            this.dataSource = dataSource;
        }
        else {
            throw new Error("Only ChartDataSources can be added.");
        }
    }
}
