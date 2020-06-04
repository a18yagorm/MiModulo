# -*- coding: utf-8 -*-
from odoo import http

# class Casas(http.Controller):
#     @http.route('/casas/casas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/casas/casas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libros.listing', {
#             'root': '/casas/casas',
#             'objects': http.request.env['casas.casas'].search([]),
#         })

#     @http.route('/casas/casas/objects/<model("casas.casas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('casas.object', {
#             'object': obj
#         })