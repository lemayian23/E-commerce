# Part of ecommerce. See LICENSE file for full copyright and licensing details.
from ecommerce.addons.account.models.chart_template import update_taxes_from_templates

def migrate(cr, version):
    update_taxes_from_templates(cr, 'l10n_at.l10n_at_chart_template')
