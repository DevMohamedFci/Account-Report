# -*- coding: utf-8 -*-
from odoo import http

# class Leadreport(http.Controller):
#     @http.route('/account_report/account_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_report/account_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_report.listing', {
#             'root': '/account_report/account_report',
#             'objects': http.request.env['account_report.account_report'].search([]),
#         })

#     @http.route('/account_report/account_report/objects/<model("account_report.account_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_report.object', {
#             'object': obj
#         })