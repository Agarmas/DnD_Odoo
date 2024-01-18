from odoo import models, fields, api

class Characteristic(models.Model):
    #Special fields
    _name = 'characteristic'
    _description = 'Characteristics for characters'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Class\'s name'
    )        
    
    classes_ids = fields.One2many(
        string='Classes',
        comodel_name='c_class',
        inverse_name='spells_characteristic_id',
    )
    
    skills_ids = fields.One2many(
        string='Skills',
        comodel_name='skill',
        inverse_name='characteristic_id',
    )
    