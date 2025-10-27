# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import logging
import ecommerce.tests
from ecommerce.addons.base.tests.common import HttpCaseWithUserDemo

_logger = logging.getLogger(__name__)


@ecommerce.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(ecommerce.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "ecommerce.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "ecommerce.isReady === true", login="admin", timeout=600)
                self.terminate_browser()


@ecommerce.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(ecommerce.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_demo(self):
        user_demo = self.env.ref("base.user_demo")
        menus = self.env['ir.ui.menu'].with_user(user_demo.id).load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "ecommerce.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "ecommerce.isReady === true", login="demo", timeout=600)
                self.terminate_browser()

@ecommerce.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(ecommerce.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "ecommerce.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "ecommerce.isReady === true", login="admin", timeout=120)

@ecommerce.tests.tagged('post_install', '-at_install',)
class TestMenusDemoLight(HttpCaseWithUserDemo):
    allow_end_on_form = True

    def test_01_click_apps_menus_as_demo(self):
        # If not enabled (like in demo data), landing on website dashboard will redirect to /
        # and make the test crash
        group_website_designer = self.env.ref('website.group_website_designer', raise_if_not_found=False)
        if group_website_designer:
            self.env.ref('base.group_user').write({"implied_ids": [(4, group_website_designer.id)]})
        self.browser_js("/web", "ecommerce.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "ecommerce.isReady === true", login="demo", timeout=120)
