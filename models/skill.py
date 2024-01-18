from odoo import models, fields, api

class Skill(models.Model):
    #Special fields
    _name = 'skill'
    _description = 'Skills'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Skill\'s name'
    )        
    
    characteristic_id = fields.Many2one(
        string='Characteristic',
        comodel_name='characteristic',
        ondelete='restrict',
    )
    
    