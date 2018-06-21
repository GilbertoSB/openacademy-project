# -*- coding: utf-8 -*-

from odoo import models, fields, api
'''
This module create module of course
'''

class Course(models.Model):
	'''
	This class create model of course
	'''
	_name = 'openacademy.course' # Nombre del modelo en odoo

	# Campo reservado para identificar el registro
	name = fields.Char(string='Title', required =True)
	description = fields.Text(string='Description')
