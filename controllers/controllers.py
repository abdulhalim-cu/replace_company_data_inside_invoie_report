# -*- coding: utf-8 -*-
from odoo import http

# class CompanyLogo(http.Controller):
#     @http.route('/company_logo/company_logo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_logo/company_logo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_logo.listing', {
#             'root': '/company_logo/company_logo',
#             'objects': http.request.env['company_logo.company_logo'].search([]),
#         })

#     @http.route('/company_logo/company_logo/objects/<model("company_logo.company_logo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_logo.object', {
#             'object': obj
#         })