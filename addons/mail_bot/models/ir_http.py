# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user._is_internal():
            res['ecommercebot_initialized'] = self.env.user.ecommercebot_state not in [False, 'not_initialized']
        return res
