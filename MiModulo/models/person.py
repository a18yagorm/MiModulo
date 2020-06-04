# -*- coding: utf-8 -*-

import time
from datetime import datetime, date
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta

class person(models.Model):
	_name = 'houses.person'
	_inherits = {'res.partner': 'partner_id'}

	partner_id = fields.Many2one('res.partner', ondelete='cascade')
	name = fields.Char(string='Nombre', required=True)
	age = fields.Integer(compute="calcular_edad", string='Edad')

	@api.depends('person_dob')
	def calcular_edad(self):
		if self.person_dob:
			dob = self.person_dob.strftime("%Y")
			t = datetime.now()
			today = t.strftime("%Y")
			edad = int(today) - int(dob)
			#edad = relativedelta(date.today, self.person_dob).years
			self.age = edad

	photo = fields.Binary(string='Foto')
	gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')], string='Género')
	house_ids = fields.One2many('houses.house', inverse_name='owner_id', string='Casas en propiedad')
	person_dob = fields.Date(string="Fecha de Nacimiento")
	person_job = fields.Char(string="Trabajo", required=False)
	nationality = fields.Many2one('res.country', string='Nacionalidad')
	person_blood_type = fields.Selection(
    	[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'),
     	('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')],
    	string='Grupo de sangre')
	owned_houses = fields.Integer('Casas en propiedad', compute='_num_casas', store=False)

	@api.depends('house_ids')
	def _num_casas(self):
		for record in self:
			record.owned_houses = len(record.house_ids)