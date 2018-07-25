# -*- coding:utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import email_split, float_is_zero

class hrexpense_inherit(models.Model):
    _inherit = 'hr.expense'

    partner_id = fields.Many2one(comodel_name='res.partner', string='供應商')

    @api.multi
    def submit_expenses(self):
        res = super(hrexpense_inherit, self).submit_expenses()
        res['context']['default_partner_id'] = self[0].partner_id.id
        return res

    def _prepare_move_line(self, line):
        res = super(hrexpense_inherit, self)._prepare_move_line(line)
        if res['debit'] > 0:
            expense_id = self.env['hr.expense'].browse(res['partner_id'])
            res['partner_id'] = expense_id.partner_id.id                       #這裡沒寫入
            if expense_id.partner_id.name:
                res['name'] = expense_id.partner_id.name + ': '+ expense_id.name
        return res

    class HrExpenseSheet(models.Model):
        _inherit = "hr.expense.sheet"

        partner_id = fields.Many2one(comodel_name='res.partner', string='供應商')

