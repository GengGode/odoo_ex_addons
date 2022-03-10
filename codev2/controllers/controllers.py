# -*- coding: utf-8 -*-
from odoo import http

# class Codev2(http.Controller):
#     @http.route('/codev2/codev2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/codev2/codev2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('codev2.listing', {
#             'root': '/codev2/codev2',
#             'objects': http.request.env['codev2.codev2'].search([]),
#         })

#     @http.route('/codev2/codev2/objects/<model("codev2.codev2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('codev2.object', {
#             'object': obj
#         })