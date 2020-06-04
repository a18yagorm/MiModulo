# -*- coding: utf-8 -*-
{
    'name': "Propiedades",
    'summary': """
        Control de casas e propietarios""",
    'description': """
        Control de casas e propietarios
    """,
    'author': "Yago Ramas",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_casa.xml',
        'views/view_persona.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}