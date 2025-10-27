/** @ecommerce-module */

import spreadsheet from "@spreadsheet/o_spreadsheet/o_spreadsheet_extended";

const { chartComponentRegistry } = spreadsheet.registries;
const { ChartJsComponent } = spreadsheet.components;

chartComponentRegistry.add("ecommerce_bar", ChartJsComponent);
chartComponentRegistry.add("ecommerce_line", ChartJsComponent);
chartComponentRegistry.add("ecommerce_pie", ChartJsComponent);

import ecommerceChartCorePlugin from "./plugins/ecommerce_chart_core_plugin";
import ChartecommerceMenuPlugin from "./plugins/chart_ecommerce_menu_plugin";
import ecommerceChartUIPlugin from "./plugins/ecommerce_chart_ui_plugin";

export { ecommerceChartCorePlugin, ChartecommerceMenuPlugin, ecommerceChartUIPlugin };
