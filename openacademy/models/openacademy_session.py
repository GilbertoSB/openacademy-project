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