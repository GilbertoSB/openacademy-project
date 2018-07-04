# -*- coding: utf-8 -*-

from odoo import fields, models

class Session(models.Model):
    '''
    Esta clase crea el modweo de Cesiones
    '''
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string='Instructor', 
                                    domain=['|',
                                            ('instructor','=',True),
                                            ('category_id.name','ilike',"Teacher")])
    course_id = fields.Many2one('openacademy.course', 
                ondelete='cascade',  string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")