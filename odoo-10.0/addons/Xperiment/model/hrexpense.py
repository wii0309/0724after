# -*- coding:utf-8 -*-
from odoo import api, fields, models

class hrexpense_inherit(models.Model):
    _inherit = 'hr.expense'

    partner_id = fields.Many2one(comodel_name='res.partner', string='供應商')

    def _prepare_move_line(self, line):
        res = super(hrexpense_inherit, self)._prepare_move_line(line)
        if res['debit'] > 0:
            res['partner_id'] = self.partner_id.id
            if self.partner_id:
                res['name'] = self.partner_id.name + ': '+ self.name
        return res