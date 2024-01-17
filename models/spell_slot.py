from odoo import models, fields, api


class SpellSlot(models.Model):
    #Special fields
    _name = 'spell_slot'
    _description = 'Character\'s spell slots'

    # Fields
    ss_level = fields.Integer(
        string='ss_level',
    )
    
    ss_qty = fields.Integer(
        string='ss_qty',
    )
    
    character_id = fields.Many2one(
        string='Character',
        comodel_name='character',
        ondelete='restrict',
    )
    
    
    # SQL constraints
    _sql_constraints = [
    ('max_ss_level_9', 'CHECK (ss_level <= 9)', '9 is de higest number for spell slot level'),
]