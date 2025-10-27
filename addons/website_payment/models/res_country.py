# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import api, fields, models

from ecommerce.addons.payment_stripe import const


class ResCountry(models.Model):
    _inherit = 'res.country'

    is_stripe_supported_country = fields.Boolean(compute='_compute_is_stripe_supported_country')

    @api.depends('code')
    def _compute_is_stripe_supported_country(self):
        for country in self:
            country.is_stripe_supported_country = const.COUNTRY_MAPPING.get(
                country.code, country.code
            ) in const.SUPPORTED_COUNTRIES
