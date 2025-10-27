# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import fields, models


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    costs_hour_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account',
        help="Posts analytical accounting entries in real time for both component and operational costs.")
