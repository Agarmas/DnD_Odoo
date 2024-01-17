from odoo import models, fields, api

class C_Class(models.Model):
    #Special fields
    _name = 'c_class'
    _description = 'Classes for characters'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Class\'s name'
    )

    
    spells_characteristic_id = fields.Many2one(
        string='Spells characteristic',
        comodel_name='characteristic',
        ondelete='restrict',
    )
    