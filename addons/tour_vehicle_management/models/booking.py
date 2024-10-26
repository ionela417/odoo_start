from odoo import models, fields, api

class TourBooking(models.Model):
    _inherit = 'tour.booking'

    vehicle_id = fields.Many2one('tour.vehicle', string='Assigned Vehicle')

    @api.onchange('vehicle_id')
    def _check_vehicle_availability(self):
        # Filtra i veicoli disponibili
        available_vehicles = self.env['tour.vehicle'].search([('is_available', '=', True)])
        return {'domain': {'vehicle_id': [('id', 'in', available_vehicles.ids)]}}