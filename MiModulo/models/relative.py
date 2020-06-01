# -*- coding: utf-8 -*-

import time
from datetime import datetime, date
from odoo import api,models, fields
from dateutil.relativedelta import relativedelta

class Person(models.Model):
	_name = 'person.person'
	_description = 'Grava Información de los familiares'

	name = fields.Char(string='Nombre', required=True)
	age = fields.Integer(compute="calcular_edad", string='Edad')
	photo = fields.Binary(string='Foto')
	relative_type = fields.Char(string="Tipo de familiar(Padres,madre,...)", required=True)
	gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')], string='Género')
	person_dob = fields.Date(string="Fecha de Nacimiento")
	person_doe = fields.Date(string="Dia de saida")
	person_job = fields.Char(string="Trabajo", required=False)
	nationality = fields.Many2one('res.country', string='Nacionalidad')

	@api.depends('person_dob')
	def calcular_edad(self):
		if self.person_dob:
			dob = self.person_dob.strftime("%Y")
			t = datetime.now()
			today = t.strftime("%Y")
			edad = int(today) - int(dob)
			#edad = relativedelta(date.today, self.person_dob).years
			self.age = edad