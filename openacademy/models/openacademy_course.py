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
    responsible_id = fields.Many2one('res.users', 
                        ondelete='set null', string='Responsible', index = True)
    session_ids = fields.One2many('openacademy.session',
                        'course_id', 
                        string='Sessions')