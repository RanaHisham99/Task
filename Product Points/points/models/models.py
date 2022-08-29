# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductPoints(models.Model):
    _name = 'product.points'

    name = fields.Char(string='Product Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    points = fields.Integer(string='Points')
    Status = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'),
                               ('ended','Ended')])
    user_id = fields.Many2one('res.users', ondelete='set null', string="Last Change Status By",
                     index=True)  #Last updated by



