# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_restaurant_printer(self):
        result = super()._loader_params_restaurant_printer()
        result['search_params']['fields'].append('epson_printer_ip')
        return result
