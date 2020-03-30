# -*- coding: utf-8 -*-

from odoo import models, fields

class Person(models.Model):
	_name = 'person.person'

	name = fields.Char(string='Nombre', required=True)
	age = fields.Integer(string='Edad')
	photo = fields.Binary(string='Foto')
	gender = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string='Género')
	person_dob = fields.Date(string="Fecha de Nacimiento")
	nationality = fields.Many2one('res.country', string='Nacionalidad')