/** @ecommerce-module */

import { Component } from "@ecommerce/owl";
import { DROPDOWN } from "@web/core/dropdown/dropdown";

export class KanbanDropdownMenuWrapper extends Component {
    onClick(ev) {
        this.env[DROPDOWN].closeAllParents();
    }
}
KanbanDropdownMenuWrapper.template = "web.KanbanDropdownMenuWrapper";
