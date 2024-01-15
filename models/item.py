from odoo import models, fields, api


class Item(models.Model):
    #Special fields
    _name = 'item'
    _description = 'Posible items in the game'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Item\'s name'
    )

    type1 = fields.Char(
        string='First type', 
        size=255, 
        help='Item\'s type1'
    )

    type2 = fields.Char(
        string='Second type',
        size=255,
        help='Item\'s type2'
    )

    weight = fields.Integer(
        string='Weight',
        help='Item\'s weight (lbs)' 
    )

    price = fields.Integer(
        string='Price',
        help='Item\'s price (PO)'
    )       
    
    description = fields.Text(
        string='Description',
        help='Item\'s description'
    )
    