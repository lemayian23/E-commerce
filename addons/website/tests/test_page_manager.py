# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import json

import ecommerce.tests

from ecommerce.tests.common import HOST
from ecommerce.tools import config


@ecommerce.tests.common.tagged('post_install', '-at_install')
class TestWebsitePageManager(ecommerce.tests.HttpCase):

    def test_01_page_manager(self):
        website = self.env['website'].create({
            'name': 'Test Website',
            'domain': '',
            'sequence': 20
        })
        url = self.env['website'].get_client_action_url('/')
        self.start_tour(url, 'website_page_manager', login="admin")
        self.start_tour(url, 'website_page_manager_session_forced', login="admin", cookies={
            'websiteIdMapping': json.dumps({'Test Website': website.id})
        })

        website.domain = f'http://{HOST}:{config["http_port"]}'
        self.start_tour('/web#action=website.action_website_pages_list', 'website_page_manager_direct_access', login='admin')
