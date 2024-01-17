from odoo import models, fields, api


class Spell(models.Model):
    #Special fields
    _name = 'spell_slot'
    _description = 'Character\'s spell slots'

    # Fields
    ss_level = fields.Integer(
        string='ss_level',
    )
    
    ss_qty = fields.Char(
        string='ss_qty',
    )
    