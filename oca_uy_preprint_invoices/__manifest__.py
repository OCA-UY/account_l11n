# -*- coding: utf-8 -*-
{
    'name': "oca_uy_preprint_invoices",

    'summary': u"Módulo base para usar preimpresos de factura",

    'description': u"""
        crea la posibildiad de imprimir en la factura los preimpresos
        brinda un template estándar para un preimpreso en a4 y acciones en
        el botón imprimir
    """,

    'author': "Odoo Community Association - Uruguay",
    'website': "http://www.oca.org.uy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'uy',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['account','base_vat'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
