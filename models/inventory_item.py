from odoo import models, fields, api

class InventoryItem(models.Model):
    # Special fields
    _name = 'inventory_item'
    _description = 'Char Value'

    # Fields
    character_id = fields.Many2one(
        'character',
        string='Character',
        required=True
    )

    item_id = fields.Many2one(
        'item',
        string='Item',
        required=True
    )

    amount = fields.Integer(
        string='Amount',
        default=1,
    )

    # Sql conctraints
    _sql_constraints = [
        ('unique_inventory_item', 'unique(character_id, item_id)', 'The combination of Character and Item must be unique!'),
    ]
    