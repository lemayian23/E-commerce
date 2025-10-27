# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import ecommerce


def db_list(force=False, host=None):
    return []

ecommerce.http.db_list = db_list
