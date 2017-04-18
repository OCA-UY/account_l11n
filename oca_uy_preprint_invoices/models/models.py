# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class oca_uy_preprint_invoices(models.Model):
#     _name = 'oca_uy_preprint_invoices.oca_uy_preprint_invoices'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _get_tax_amount_by_tax(self):
        self.ensure_one()
        res = {}
        res.setdefault(self.env['account.tax'].search([('name', 'ilike', '%Ventas (10%')]), [0.0, 0.0])
        res.setdefault(self.env['account.tax'].search([('name', 'ilike', '%Ventas (22%')]), [0.0, 0.0])
        res.setdefault(self.env['account.tax'].search([('name', 'ilike', '%Ventas Exentos%')]), [0.0, 0.0])
        currency = self.currency_id or self.company_id.currency_id
        for line in self.tax_line_ids:
            res.setdefault(line.tax_id, [0.0, 0.0])
            res[line.tax_id][0] += line.base
            res[line.tax_id][1] += line.amount
        res = sorted(res.items(), key=lambda l: l[0].sequence)
        res = map(lambda l: (l[1][0], l[1][1]), res)
        return res
