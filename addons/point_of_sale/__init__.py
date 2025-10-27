# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers
from . import report
from . import wizard

from ecommerce import api, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    #The search domain is based on how the sequence is defined in the _get_sequence_values method in /addons/point_of_sale/models/stock_warehouse.py
    env['ir.sequence'].search([('name', 'ilike', '%Picking POS%'), ('prefix', 'ilike', '%/POS/%')]).unlink()
