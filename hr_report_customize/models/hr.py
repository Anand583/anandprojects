# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def print_report(self):
        return self.env.ref('hr_report_customize.action_report_payroll').report_action([])
