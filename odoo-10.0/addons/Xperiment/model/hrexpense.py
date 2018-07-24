# -*- coding:utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import email_split, float_is_zero

class hrexpense_inherit(models.Model):
    _inherit = 'hr.expense'

    supplier = fields.Many2one(comodel_name='res.partner', string='供應商')

    @api.multi
    def correct(self):
        for line in hr.expense.line_ids:
            if line.debit!=0:
                line.partner_id=line.supplier.id

















    #沒用程式碼
    # name= fields.Text('備註' ,compute='overr',store=True)
    #
    # state =fields.Char(string='',related='hr.expense.sheet.state')
    # @api.depends('state')
    # def overr(self):
    #     if self.state=='post':
    #         self.name="供應商名稱:"+self.supplier+"費用單據:"+self.name