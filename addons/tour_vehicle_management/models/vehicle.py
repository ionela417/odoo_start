from odoo import models, fields

class TourVehicle(models.Model):
    _name = 'tour.vehicle'
    _description = 'Tour Vehicle'

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate')
    capacity = fields.Integer(string='Capacity')
    is_available = fields.Boolean(string='Available', default=True)