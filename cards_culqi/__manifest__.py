# -*- coding: utf-8 -*-
{
    'name': 'Culqi Tarjetas - Website Checkout',
    'description': "Recibe pagos con tarjetas a través del sitio web de comercio electrónico en divisa PEN & USD",
    'author': "ROCKSCRIPTS",
    'website': "http://13culqi.microdoo.co",
    'summary': "Culqi para sitio web de comercio electrónico",
    'version': '0.1',
    "license": "OPL-1",
    'price':'100',
    'currency':'USD',
    'support': 'rockscripts@gmail.com',
    'category': 'Website',
    "images": ["images/banner.png"],
    'depends': ['base','sale','website','website_sale','payment','account'],
    'data': [
                'views/templates.xml',
                'views/payment_acquirer.xml',
                'views/sale_order.xml',
                'views/payment_transaction.xml',
                'views/partner.xml',
                'data/culqi.xml',
            ],
    'qweb': [
              
            ],
    'installable': True,
}