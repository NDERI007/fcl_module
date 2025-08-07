# -*- coding: utf-8 -*-
{
    'name': "fcl_module",
    'summary': "Custom pos logic with paystack integration",
    'author': "FCL Services",
    'website': "https://www.yourcompany.com",

    'category': 'Point of Sale',
    'version': '0.1',

    'depends': ['point_of_sale', 'pos_restaurant', 'stock'],

    'data': [
        'views/payment_method.xml',
    ],

    'assets': {
        'web.assests_common': [
            'fcl_module/static/src/js/model.js',
            'fcl_module/static/src/js/paystack_test.js',
        ]
    },

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}