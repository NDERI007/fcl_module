# -*- coding: utf-8 -*-
{
    'name': "fcl_module",
    'summary': "Custom pos logic with paystack integration",
    'author': "FCL Services",
    'website': "https://www.yourcompany.com",

    'category': 'Point of Sale',
    'version': '0.1',

    'depends': ['point_of_sale', 'pos_restaurant', 'stock'],

    'assets': {
        'point_of_sale._assets_pos': [
            'fcl_module/static/src/scss/custom_styles.scss',
        ]
    },

    'installable': True,
    'application': True,
}