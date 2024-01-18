import math
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CharValue(models.Model):
    # Special fields
    _name = 'your_module.char_value'
    _description = 'Char Value'

    # Fields
    character_id = fields.Many2one(
        'character',
        string='Character',
        required=True
    )

    characteristic_id = fields.Many2one(
        'characteristic',
        string='Characteristic',
        required=True
    )

    value = fields.Integer(
        string='Value',   
    )

    modifier = fields.Integer(
        string='Modifier',
        store=True,
        compute='_compute_modifier',
    )

    # Sql conctraints
    _sql_constraints = [
        ('unique_characteristic_value', 'unique(character_id, characteristic_id)', 'The combination of Character and Characteristic must be unique!'),
    ]

    # Computed
    @api.depends('value')
    def _compute_modifier(self):
        for record in self:
            record.modifier = math.floor((self.value - 10) / 2) 
    
    