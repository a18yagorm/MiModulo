# -*- coding: utf-8 -*-
{
	'name': 'Propietarios',
	'version': '12.0.1.0.0',
	'summary': 'Controla casas e os seus propietarios',
	'category': 'Tools',
	'author': 'Yago Ramas',
	'maintainer': 'Yago Ramas',
	'company': '',
	'website': '',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
    	'views/person_view.xml',
		'views/house_view.xml'
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}