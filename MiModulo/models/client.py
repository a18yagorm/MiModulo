# -*- coding: utf-8 -*-

from odoo import models, fields

class Client(models.Model):
	_name = 'client.client'

	name = fields.Char(string='Name', required=True)
	age = fields.Integer(string='Age')
	photo = fields.Binary(string='Image')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Discharge Date")

	nationality = fields.Many2one('res.country', string='Nationality')