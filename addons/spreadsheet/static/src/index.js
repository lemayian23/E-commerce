/** @ecommerce-module */

/**
 * This file is meant to load the different subparts of the module
 * to guarantee their plugins are loaded in the right order
 *
 * dependency:
 *             other plugins
 *                   |
 *                  ...
 *                   |
 *                filters
 *                /\    \
 *               /  \    \
 *           pivot  list  ecommerce chart
 */

/** TODO: Introduce a position parameter to the plugin registry in order to load them in a specific order */
import spreadsheet from "@spreadsheet/o_spreadsheet/o_spreadsheet_extended";
const { corePluginRegistry, uiPluginRegistry } = spreadsheet.registries;

import { GlobalFiltersCorePlugin, GlobalFiltersUIPlugin } from "@spreadsheet/global_filters/index";
import { PivotCorePlugin, PivotUIPlugin } from "@spreadsheet/pivot/index"; // list depends on filter for its getters
import { ListCorePlugin, ListUIPlugin } from "@spreadsheet/list/index"; // pivot depends on filter for its getters
import {
    ChartecommerceMenuPlugin,
    ecommerceChartCorePlugin,
    ecommerceChartUIPlugin,
} from "@spreadsheet/chart/index"; // ecommercechart depends on filter for its getters

corePluginRegistry.add("ecommerceGlobalFiltersCorePlugin", GlobalFiltersCorePlugin);
corePluginRegistry.add("ecommercePivotCorePlugin", PivotCorePlugin);
corePluginRegistry.add("ecommerceListCorePlugin", ListCorePlugin);
corePluginRegistry.add("ecommerceChartCorePlugin", ecommerceChartCorePlugin);
corePluginRegistry.add("chartecommerceMenuPlugin", ChartecommerceMenuPlugin);

uiPluginRegistry.add("ecommerceGlobalFiltersUIPlugin", GlobalFiltersUIPlugin);
uiPluginRegistry.add("ecommercePivotUIPlugin", PivotUIPlugin);
uiPluginRegistry.add("ecommerceListUIPlugin", ListUIPlugin);
uiPluginRegistry.add("ecommerceChartUIPlugin", ecommerceChartUIPlugin);
