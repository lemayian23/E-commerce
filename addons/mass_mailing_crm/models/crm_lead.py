# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
