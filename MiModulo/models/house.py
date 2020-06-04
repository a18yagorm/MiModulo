# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class house(models.Model):
	_name = 'houses.house'

	location = fields.Char(string='Dirección', required=True)
    owner_id = fields.Many2one('houses.person', string='Propietario', required=True)
	photo = fields.Binary(string='Foto')
    meters = fields.Char(string='Metros cuadrados')
    
