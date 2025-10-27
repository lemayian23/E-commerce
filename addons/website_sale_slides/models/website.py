# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models
from ecommerce.osv import expression


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return expression.AND([
            super(Website, self).sale_product_domain(),
            [('detailed_type', '!=', 'course')],
        ])
