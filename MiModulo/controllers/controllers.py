# -*- coding: utf-8 -*-
from odoo import http

# class Houses(http.Controller):
#     @http.route('/houses/houses/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/houses/houses/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('houses.listing', {
#             'root': '/houses/houses',
#             'objects': http.request.env['houses.houses'].search([]),
#         })

#     @http.route('/houses/houses/objects/<model("houses.houses"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('houses.object', {
#             'object': obj
#         })