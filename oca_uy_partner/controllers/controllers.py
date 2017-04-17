# -*- coding: utf-8 -*-
from odoo import http

# class OcaUyPartner(http.Controller):
#     @http.route('/oca_uy_partner/oca_uy_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_uy_partner/oca_uy_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_uy_partner.listing', {
#             'root': '/oca_uy_partner/oca_uy_partner',
#             'objects': http.request.env['oca_uy_partner.oca_uy_partner'].search([]),
#         })

#     @http.route('/oca_uy_partner/oca_uy_partner/objects/<model("oca_uy_partner.oca_uy_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_uy_partner.object', {
#             'object': obj
#         })