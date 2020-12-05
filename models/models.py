# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True, help="Name of Course")
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsiable", index=True)

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Academy Sessions"

    name = fields.Char(requied=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)