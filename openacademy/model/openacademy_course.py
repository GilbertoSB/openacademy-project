from odoo import models, fields, api
'''
This module create model of course
'''


class Course(models.Model):
    '''
    This class create model of course
    '''

    _name = 'openacademy.course' # Nombre del modelo (tabla)

    name = fields.Char(string='Title', required=True) # Campo reservado para idenditificar  el nombre del registro
    description = fields.Text(string='Description')
