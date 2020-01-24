# -*- coding: utf-8 -*-
from odoo import http

# class MiroDaniel(http.Controller):
#     @http.route('/miro_daniel/miro_daniel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miro_daniel/miro_daniel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('miro_daniel.listing', {
#             'root': '/miro_daniel/miro_daniel',
#             'objects': http.request.env['miro_daniel.miro_daniel'].search([]),
#         })

#     @http.route('/miro_daniel/miro_daniel/objects/<model("miro_daniel.miro_daniel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miro_daniel.object', {
#             'object': obj
#         })