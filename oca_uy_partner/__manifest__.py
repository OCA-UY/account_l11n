# -*- coding: utf-8 -*-
{
    'name': "oca_uy_partner",

    'summary': u"""
        partner: localización Uruguay
        """,

    'description': u"""
        Cambios al partner para agregar RUT y a futuro otros cambios requeridos para uruguay
    """,

    'author': "Odoo Community Association - Uruguay",
    'website': "http://www.oca.org.uy",

    'category': 'uy',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}
