import requests

from odoo import http
from odoo.http import request
from datetime import datetime
from num2words import num2words
import urllib.parse as urlparse
from urllib.parse import parse_qs
from odoo import models, fields, api
from odoo import api, fields, models, _


class VehicleRequest(models.Model):
    _inherit = 'vehicle.request'

    basic_synch_v_req = fields.Char(string="Vehicle Request Synchronius")
    basic_synch_vehi_req = fields.Char(string="Vehicle Request Synchronius")
    basic_synch_v_req_approval = fields.Char(string="Vehicle Request Synchronius")
    basic_synch_v_req_button = fields.Boolean(string="Vehicle Request Synchronius")


class RouteKmSetUp(models.Model):
    _inherit = 'route.km.set.up'

    basic_synch_route_km = fields.Char(string="Vehicle Request Synchronius")
    basic_synch_route_km_button = fields.Boolean(string="Vehicle Request Synchronius")


class BranchCodeConfig(models.Model):
    _inherit = 'branch.code.config'


    basic_synch_branch_code = fields.Char(string="branch Code Synchronius")
    basic_synch_branch_code_button = fields.Boolean(string="Branch Code Synchronius")


    #
    # @api.constrains('basic_synch_branch_code_button')
    # def basic_basic_synch_branch_code_button(self):
    #     if self.basic_synch_branch_code_button:
    #         self.create_code()



class VehicleRequsetApproval(models.Model):
    _inherit = 'vehicle.requset.approval'

    basic_synch_v_req_approval = fields.Char(string="branch Code Synchronius")
    basic_synch_v_req = fields.Char(string="Vehicle Request Synchronius")
    basic_synch_v_req_approval_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_v_req_appr_che_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_v_req_appr_exter_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_alloc_vehi_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_alloc_vehi_button_test = fields.Boolean(string="Branch Code Synchronius")



class GeneratePass(models.Model):
    _inherit = 'generate.pass'

    basic_synch_generate_pass = fields.Char(string="branch Code Synchronius")
    basic_synch_generate_pass_button = fields.Boolean(string="Branch Code Synchronius")




class AdvanceConfig(models.Model):
    _inherit = 'advance.config'

    basic_synch_advance_config = fields.Char(string="branch Code Synchronius")
    basic_synch_advance_config_button = fields.Boolean(string="Branch Code Synchronius")

    # @api.constrains('basic_synch_advance_config_button')
    # def basic_basic_synch_advance_config_button(self):
    #     if self.basic_synch_advance_config_button:
    #         self.allote_pass_new()



class LoadingConfig(models.Model):
    _inherit = 'loading.config'

    basic_synch_loading_config = fields.Char(string="branch Code Synchronius")
    basic_synch_loading_config_button = fields.Boolean(string="Branch Code Synchronius")



class GenerateOutPassRequest(models.Model):
    _inherit = 'generate.out.pass.request'


    basic_synch_out_pass = fields.Char(string="branch Code Synchronius")
    basic_synch_out_pass_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_out_pass_button_test = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_update_datas_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_post_entries_button = fields.Boolean(string="Branch Code Synchronius")



class FuelType(models.Model):
    _inherit = 'fuel.type'

    basic_synch_fuel_type = fields.Char(string="branch Code Synchronius")
    basic_synch_fuel_type_button = fields.Boolean(string="Branch Code Synchronius")



class UpdateStatus(models.Model):
    _inherit = 'update.status'

    basic_synch_update_status = fields.Char(string="branch Code Synchronius")
    basic_synch_update_status_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_update_sta_halt_button = fields.Boolean(string="Branch Code Synchronius")
    vehicle_id_halt = fields.Many2one('fleet.vehicle')
    location_halt = fields.Char()
    reason_halt = fields.Char()


class VehilcleHalt(models.TransientModel):
    _inherit = 'vehicle.halt'

    basic_synch_update_halt_status = fields.Char(string="branch Code Synchronius")
    basic_synch_update_halt_button = fields.Boolean(string="Branch Code Synchronius")



class MtcExpenseDetails(models.Model):
    _inherit = 'mtc.expense.details'

    basic_synch_mtc_expense = fields.Char(string="branch Code Synchronius")
    basic_synch_mtc_expense_button = fields.Boolean(string="Branch Code Synchronius")


class InternalPumbPayments(models.Model):
    _inherit = 'internal.pumb.payment'

    basic_synch_internal_expense = fields.Char(string="branch Code Synchronius")
    basic_synch_internal_expense_button = fields.Boolean(string="Branch Code Synchronius")




class BranchExpenses(models.Model):
    _inherit = 'branch.expenses'

    basic_synch_branch_expenses = fields.Char(string="branch Code Synchronius")
    basic_synch_branch_expenses_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_branch_app_expenses_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_post_expense_button = fields.Boolean(string="Branch Code Synchronius")

class ReciptForm(models.Model):
    _inherit = 'recipt.form'


    basic_synch_recipt_form = fields.Char(string="branch Code Synchronius")
    basic_synch_recipt_form_button = fields.Boolean(string="Branch Code Synchronius")

class AdvanceInternalTransfer(models.Model):
    _inherit = 'advance.internal.transfer'
    basic_synch_advance_inter = fields.Char(string="branch Code Synchronius")
    basic_synch_advance_inter_button = fields.Boolean(string="Branch Code Synchronius")

class SecondAdvance(models.Model):
    _inherit = 'second.advance'



    basic_synch_second_advance = fields.Char(string="branch Code Synchronius")
    basic_synch_second_advance_button = fields.Boolean(string="Branch Code Synchronius")

class OpeningBalanceBranch(models.Model):
    _inherit = 'opening.balance.branch'

    basic_synch_op_bal_branch = fields.Char(string="branch Code Synchronius")
    basic_synch_op_bal_branch_button = fields.Boolean(string="Branch Code Synchronius")


class BranchLoan(models.Model):
    _inherit = 'branch.loan'


    basic_synch_branch_loan = fields.Char(string="branch Code Synchronius")
    basic_synch_branch_loan_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_pay_loan_button = fields.Boolean(string="Branch Code Synchronius")

class AdvanceApproval(models.Model):
    _inherit = 'advance.approval'


    basic_synch_advance_approval = fields.Char(string="branch Code Synchronius")
    basic_synch_advance_approval_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_advance_reject_button = fields.Boolean(string="Branch Code Synchronius")

class FuelPaymentForm(models.Model):
    _inherit = 'fuel.payment.form'



    basic_synch_fuel_payment = fields.Char(string="branch Code Synchronius")
    basic_synch_fuel_payment_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_fuel_pay_bill_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_fuel_cancel_bill_button = fields.Boolean(string="Branch Code Synchronius")


class FreightTemplate(models.Model):
    _inherit = "freight.template"
    basic_synch_freight_tmp = fields.Char(string="branch Code Synchronius")
    basic_synch_freight_tmp_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_freight_approve_button = fields.Boolean(string="Branch Code Synchronius")


class RtgsPaymentForm(models.Model):
    _inherit = 'rtgs.payment.form'

    basic_synch_rtgs_payment = fields.Char(string="branch Code Synchronius")
    basic_synch_rtgs_payment_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_rtgs_payment_app_button = fields.Boolean(string="Branch Code Synchronius")
    basic_synch_rtgs_payment_paid_button = fields.Boolean(string="Branch Code Synchronius")

class BettaForm(models.Model):
    _inherit = 'betta.form'

    basic_synch_betta_form = fields.Char(string="branch Code Synchronius")
    basic_synch_betta_form_button = fields.Boolean(string="Branch Code Synchronius")

class TripSheet(models.Model):
    _inherit = 'trip.sheet'

    basic_synch_trip_sheet = fields.Char(string="branch Code Synchronius")
    basic_synch_trip_sheet_button = fields.Boolean(string="Branch Code Synchronius")


class HrEmployeePrivate(models.Model):
    _inherit = 'hr.employee'


    basic_synch_hr_employee = fields.Char(string="branch Code Synchronius")
    basic_synch_hr_employee_button = fields.Boolean(string="Branch Code Synchronius")


class PayLoanWizard(models.Model):
    _inherit = 'pay.loan.wizard'


    basic_synch_pay_loan_wizard = fields.Char(string="branch Code Synchronius")
    basic_synch_pay_loan_wizard_button = fields.Boolean(string="Branch Code Synchronius")


class TripSheet(models.Model):
    _inherit = 'trip.sheet'


class VehicleRequsetMarkDone(models.Model):
    _inherit = 'vehicle.requset.mark.done'

    basic_synch_requset_mark_done = fields.Char(string="branch Code Synchronius")
    basic_synch_requset_mark_done_button = fields.Boolean(string="Branch Code Synchronius")
