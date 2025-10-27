# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers

from ecommerce import api, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    dt = env.ref('website_slides.badge_data_certification_goal', raise_if_not_found=False)
    if dt:
        dt.domain = "[('completed', '=', True), (0, '=', 1)]"
