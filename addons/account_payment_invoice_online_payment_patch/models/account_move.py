# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models
from ecommerce.tools import str2bool


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _has_to_be_paid(self):
        enabled_feature = str2bool(
            self.env['ir.config_parameter'].sudo().get_param(
                'account_payment.enable_portal_payment'
            )
        )
        return enabled_feature and super()._has_to_be_paid()
