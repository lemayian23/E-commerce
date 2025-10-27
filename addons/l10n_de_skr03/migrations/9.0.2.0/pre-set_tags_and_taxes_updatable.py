# -*- coding: utf-8 -*-

import ecommerce

def migrate(cr, version):
    registry = ecommerce.registry(cr.dbname)
    from ecommerce.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_de_skr03')
