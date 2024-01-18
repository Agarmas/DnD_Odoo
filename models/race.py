from odoo import models, fields, api

class Race(models.Model):
     # Special fields
    _name = 'race'
    _description = 'Races in the game'

    # Fields
    name = fields.Char(
        string='Name',
        size=255
    )
    
    characters_ids = fields.One2many(
        string='Characters',
        comodel_name='character',
        inverse_name='race_id',
    )
    