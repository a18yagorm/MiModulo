# -*- coding: utf-8 -*-

import time
from datetime import datetime, date
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta

class persona(models.Model):
  _name='casas.persona'
  _inherits = {'res.partner': 'partner_id'}
  _sql_constraints = [('partner_uniq', 'UNIQUE(partner_id)', 'El propietario debe ser uno solo')]
  
  partner_id = fields.Many2one('res.partner', ondelete='cascade')
  person_ids = fields.One2many('casas.casa', inverse_name='person_id', string='Casa en propiedad')
  age = fields.Integer(compute="calcular_edad", string='Edad')

  @api.depends('person_dob')
  def calcular_edad(self):
    if self.person_dob:
      dob = self.person_dob.strftime("%Y")
      t = datetime.now()
      today = t.strftime("%Y")
      edad = int(today) - int(dob)
      # edad = relativedelta(date.today, self.person_dob).years
      self.age = edad

  photo = fields.Binary(string='Foto')
  gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')], string='Género')
  nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
  person_dob = fields.Date(string="Fecha de Nacimiento")
  owned_houses = fields.Integer('Casas en propiedad', compute='_num_casas', store=False)

  @api.depends('person_ids')
  def _num_casas(self):
      for record in self:
        record.owned_houses = len(record.person_ids)


    
