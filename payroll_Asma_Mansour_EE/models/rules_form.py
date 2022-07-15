from odoo import fields, models, api


class HrRules(models.Model):
    _inherit = "hr.salary.rule"
    _description = "Rules"

    nombre_des_heures = fields.Boolean(string='Nombre des heures', default=False,
                                        help="Used to display the salary rule on payslip.")
    retenues = fields.Boolean(string='Retenues', default=False,
                                       help="Used to display the salary rule on payslip.")
    remuneration = fields.Boolean(string='Rémunération', default=False,
                                       help="Used to display the salary rule on payslip.")
