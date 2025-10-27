# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import ecommerce.tests
from ecommerce.addons.gamification.tests.common import HttpCaseGamification


@ecommerce.tests.tagged('post_install', '-at_install')
class TestWebsiteProfile(HttpCaseGamification):
    def test_save_change_description(self):
        ecommerce.tests.new_test_user(
            self.env, 'test_user',
            karma=100, website_published=True
        )
        self.start_tour("/", 'website_profile_description', login="admin")
