from odoo import models, fields, api


class SpellSlot(models.Model):
    #Special fields
    _name = 'spell_slot'
    _description = 'Character\'s spell slots'

    # Fields
    ss_level = fields.Integer(
        string='Spell slot level',
    )
     
    ss_max = fields.Integer(
        string='Max slots',
    )
    
    ss_qty = fields.Integer(
        string='Spell slot quantity',
        
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

    # Checks
    @api.onchange('ss_qty')
    def _onchange_ss_qty(self):
        if self.ss_qty > self.ss_max:
            self.ss_qty = 0.0
            return {
                'warning': {
                    'title': 'Advertencia',
                    'message': 'La cantidad no puede superar la cantidad máxima. Se ha restablecido a 0.'
                }
            }