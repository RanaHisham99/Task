# -*- coding: utf-8 -*-
# from odoo import http


# class Points(http.Controller):
#     @http.route('/points/points', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/points/points/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('points.listing', {
#             'root': '/points/points',
#             'objects': http.request.env['points.points'].search([]),
#         })

#     @http.route('/points/points/objects/<model("points.points"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('points.object', {
#             'object': obj
#         })
