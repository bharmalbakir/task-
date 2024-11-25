from odoo import models, fields

class VehicleBrand(models.Model):
    _name = 'vehicle.brand'
    _description = 'Vehicle Brand'

    name = fields.Char(string='Brand Name', required=True)
    model_ids = fields.One2many('vehicle.model', 'brand_id', string='Vehicle Models')

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _description = 'Vehicle Model'

    name = fields.Char(string='Model Name', required=True)
    brand_id = fields.Many2one('vehicle.brand', string='Vehicle Brand', required=True)
    customer_id = fields.Many2one('res.partner', string="Customer")

class VehicleDetails(models.Model):
    _name = 'vehicle.details'
    _description = 'Vehicle Details'

    name = fields.Char(string="Vehicle Name")



