# from odoo import models, fields
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     vehicle_id = fields.Many2one('vehicle.master', string="Vehicle Number")
#
# from odoo import fields, models, api
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     vehicle_id = fields.Many2one('vehicle.model', string='Vehicle Number')
#
#
# @api.onchange('partner_id')
# def _onchange_partner_id(self):
#     vehicles = self.env['vehicle.master'].search([('customer_id', '=', self.partner_id.id)])
#     self.vehicle_id = vehicles
