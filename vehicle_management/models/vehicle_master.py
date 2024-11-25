
from odoo import models, fields


class VehicleMaster(models.Model):
    _name = 'vehicle.master'
    _description = 'Vehicle Master'

    vehicle_number = fields.Char(string='Vehicle Number', required=True)
    brand_name = fields.Many2one('vehicle.brand', string='Brand Name', required=True)
    model_name = fields.Many2one('vehicle.model', string='Model Name', required=True)
    owner = fields.Many2one('res.partner', string='Owner', domain=[('is_company', '=', False)], required=True)

