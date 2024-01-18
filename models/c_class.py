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
    
    proficency_save_ids = fields.Many2many(
        string='Proficency save',
        comodel_name='characteristic',
        relation='characteristic_c_class_rel',
        column1='characteristic_id',
        column2='c_class_id',
    )
        