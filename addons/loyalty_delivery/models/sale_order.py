# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_amount_total_without_delivery(self):
        self.ensure_one()
        lines = self.order_line.filtered(lambda l: l.coupon_id and l.coupon_id.program_type in ['ewallet', 'gift_card'])
        return super()._compute_amount_total_without_delivery() - sum(lines.mapped('price_unit'))
