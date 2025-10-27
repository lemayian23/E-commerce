/** @ecommerce-module */
import spreadsheet from "@spreadsheet/o_spreadsheet/o_spreadsheet_extended";
import { omit } from "@web/core/utils/objects";

const { coreTypes, helpers } = spreadsheet;
const { deepEquals } = helpers;

/** Plugin that link charts with ecommerce menus. It can contain either the Id of the ecommerce menu, or its xml id. */
export default class ChartecommerceMenuPlugin extends spreadsheet.CorePlugin {
    constructor() {
        super(...arguments);
        this.ecommerceMenuReference = {};
    }

    /**
     * Handle a spreadsheet command
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "LINK_ecommerce_MENU_TO_CHART":
                this.history.update("ecommerceMenuReference", cmd.chartId, cmd.ecommerceMenuId);
                break;
            case "DELETE_FIGURE":
                this.history.update("ecommerceMenuReference", cmd.id, undefined);
                break;
            case "DUPLICATE_SHEET":
                this.updateOnDuplicateSheet(cmd.sheetId, cmd.sheetIdTo);
                break;
        }
    }

    updateOnDuplicateSheet(sheetIdFrom, sheetIdTo) {
        for (const oldChartId of this.getters.getChartIds(sheetIdFrom)) {
            if (!this.ecommerceMenuReference[oldChartId]) {
                continue;
            }
            const oldChartDefinition = this.getters.getChartDefinition(oldChartId);
            const oldFigure = this.getters.getFigure(sheetIdFrom, oldChartId);
            const newChartId = this.getters.getChartIds(sheetIdTo).find((newChartId) => {
                const newChartDefinition = this.getters.getChartDefinition(newChartId);
                const newFigure = this.getters.getFigure(sheetIdTo, newChartId);
                return (
                    deepEquals(oldChartDefinition, newChartDefinition) &&
                    deepEquals(omit(newFigure, "id"), omit(oldFigure, "id")) // compare size and position
                );
            });

            if (newChartId) {
                this.history.update(
                    "ecommerceMenuReference",
                    newChartId,
                    this.ecommerceMenuReference[oldChartId]
                );
            }
        }
    }

    /**
     * Get ecommerce menu linked to the chart
     *
     * @param {string} chartId
     * @returns {object | undefined}
     */
    getChartecommerceMenu(chartId) {
        const menuId = this.ecommerceMenuReference[chartId];
        return menuId ? this.getters.getIrMenu(menuId) : undefined;
    }

    import(data) {
        if (data.chartecommerceMenusReferences) {
            this.ecommerceMenuReference = data.chartecommerceMenusReferences;
        }
    }

    export(data) {
        data.chartecommerceMenusReferences = this.ecommerceMenuReference;
    }
}
ChartecommerceMenuPlugin.modes = ["normal", "headless"];
ChartecommerceMenuPlugin.getters = ["getChartecommerceMenu"];

coreTypes.add("LINK_ecommerce_MENU_TO_CHART");
