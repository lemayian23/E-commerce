# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

from ecommerce.exceptions import UserError
from ecommerce.tools import config

from ecommerce.addons.payment import setup_provider, reset_payment_provider


def pre_init_hook(cr):
    if not any(config.get(key) for key in ('init', 'update')):
        raise UserError(
            "This module is deprecated and cannot be installed. "
            "Consider installing the Payment Provider: Stripe module instead.")


def post_init_hook(cr, registry):
    setup_provider(cr, registry, 'ogone')


def uninstall_hook(cr, registry):
    reset_payment_provider(cr, registry, 'ogone')
