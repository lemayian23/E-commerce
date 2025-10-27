# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import api, fields, models
from ecommerce.tools.translate import html_translate


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    website_description = fields.Html(
        string="Website Description",
        compute='_compute_website_description',
        store=True, readonly=False, precompute=True,
        sanitize_overridable=True,
        sanitize_attributes=False, translate=html_translate, sanitize_form=False)

    @api.depends('partner_id', 'sale_order_template_id')
    def _compute_website_description(self):
        orders_with_template = self.filtered('sale_order_template_id')
        (self - orders_with_template).website_description = False
        for order in orders_with_template:
            order.website_description = order.sale_order_template_id.with_context(
                lang=order.partner_id.lang
            ).website_description
