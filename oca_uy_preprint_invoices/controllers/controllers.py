# -*- coding: utf-8 -*-
from odoo import http

# class OcaUyPreprintInvoices(http.Controller):
#     @http.route('/oca_uy_preprint_invoices/oca_uy_preprint_invoices/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_uy_preprint_invoices/oca_uy_preprint_invoices/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_uy_preprint_invoices.listing', {
#             'root': '/oca_uy_preprint_invoices/oca_uy_preprint_invoices',
#             'objects': http.request.env['oca_uy_preprint_invoices.oca_uy_preprint_invoices'].search([]),
#         })

#     @http.route('/oca_uy_preprint_invoices/oca_uy_preprint_invoices/objects/<model("oca_uy_preprint_invoices.oca_uy_preprint_invoices"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_uy_preprint_invoices.object', {
#             'object': obj
#         })