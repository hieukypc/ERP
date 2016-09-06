# -*- coding: utf-8 -*-
from openerp import http

class Aaamodule(http.Controller):
    @http.route('/aaamodule/aaamodule/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/aaamodule/aaamodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaamodule.listing', {
#             'root': '/aaamodule/aaamodule',
#             'objects': http.request.env['aaamodule.aaamodule'].search([]),
#         })

#     @http.route('/aaamodule/aaamodule/objects/<model("aaamodule.aaamodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaamodule.object', {
#             'object': obj
#         })