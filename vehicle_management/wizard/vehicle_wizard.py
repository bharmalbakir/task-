


from odoo import models, fields, api

class VehicleModelWizard(models.TransientModel):
    _name = 'vehicle.model.wizard'
    _description = 'Vehicle Model Wizard'

    name = fields.Char(string="Name")
    brand_id = fields.Many2one('vehicle.brand', string='Vehicle Brand', required=True)
    model_name = fields.Char(string='Model Name', required=True)

    @api.model
    def default_get(self, fields_list):
        defaults = super(VehicleModelWizard, self).default_get(fields_list)
        return defaults

    def action_create_vehicle_model(self):
        self.env['vehicle.model'].create({
            'name': self.model_name,
            'brand_id': self.brand_id.id,
        })
        return {'type': 'ir.actions.act_window_close'}
