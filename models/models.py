# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo58(models.Model):
	_name = 'odoo58.odoo58'
	_description = 'odoo58.odoo58'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	equipo = fields.Char(string='equipo',required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
