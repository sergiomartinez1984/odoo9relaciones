# -*- coding: utf-8 -*-
# from odoo import http


# class odoo704(http.Controller):
#     @http.route('/odoo704/odoo704/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo704/odoo704/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo704.listing', {
#             'root': '/odoo704/odoo704',
#             'objects': http.request.env['odoo704.odoo704'].search([]),
#         })

#     @http.route('/odoo704/odoo704/objects/<model("odoo704.odoo704"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo704.object', {
#             'object': obj
#         })
