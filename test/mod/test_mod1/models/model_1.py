# -*- coding: utf-8 -*-
from odoo import models, fields, api, http

class NewModule1(models.Model):
    _name = 'new_module.new_module1'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
    date = fields.Date(string="Date", required=False, )