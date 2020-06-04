# -*- coding: utf-8 -*-

from odoo import models, fields, api

class casa(models.Model):
    _name='casas.casa'
    
    location = fields.Char('Direccion', required=True, index=True)
    meters = fields.Char('Metros')
    pais = fields.Many2one('res.country', string='Pais')
    person_id = fields.Many2one('casas.persona', string='Propietario')