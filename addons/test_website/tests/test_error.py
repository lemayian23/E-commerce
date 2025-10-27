import ecommerce.tests
from ecommerce.tools import mute_logger


@ecommerce.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(ecommerce.tests.HttpCase):

    @mute_logger('ecommerce.addons.http_routing.models.ir_http', 'ecommerce.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
