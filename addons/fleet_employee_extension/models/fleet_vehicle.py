from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    employee_ids = fields.Many2many(
        'hr.employee', 
        string='Assigned Employees',
        relation='fleet_vehicle_hr_employee_rel',
        column1='vehicle_id',
        column2='employee_id'
    )