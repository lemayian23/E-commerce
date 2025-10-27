# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class PurchaseRequisitionCreateAlternative(models.TransientModel):
    _inherit = 'purchase.requisition.create.alternative'

    def _get_alternative_values(self):
        vals = super(PurchaseRequisitionCreateAlternative, self)._get_alternative_values()
        vals.update({
            'picking_type_id': self.origin_po_id.picking_type_id.id,
            'group_id': self.origin_po_id.group_id.id,
        })
        return vals
