# -*- coding: utf-8 -*-
# from odoo import http


# class FclModule(http.Controller):
#     @http.route('/fcl_module/fcl_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fcl_module/fcl_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fcl_module.listing', {
#             'root': '/fcl_module/fcl_module',
#             'objects': http.request.env['fcl_module.fcl_module'].search([]),
#         })

#     @http.route('/fcl_module/fcl_module/objects/<model("fcl_module.fcl_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fcl_module.object', {
#             'object': obj
#         })

