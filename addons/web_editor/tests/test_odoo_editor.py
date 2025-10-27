# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import ecommerce.tests

@ecommerce.tests.tagged("post_install", "-at_install")
class TestecommerceEditor(ecommerce.tests.HttpCase):

    def test_ecommerce_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
