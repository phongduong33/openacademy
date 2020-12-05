# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True, help="Name of Course")
    description = fields.Text()