# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models

class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def _load(self, company):
        rslt = super()._load(company)

        if company.account_fiscal_country_id in self.env.ref('base.europe').country_ids:
            company._map_eu_taxes()

        return rslt
