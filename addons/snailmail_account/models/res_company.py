# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import fields, models


class Company(models.Model):
    _inherit = "res.company"

    invoice_is_snailmail = fields.Boolean(string='Send by Post', default=False)
