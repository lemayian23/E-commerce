# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

{
    'name': 'ecommerceBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add ecommerceBot in discussions',
    'website': 'https://www.ecommerce.com/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/ecommercebot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
