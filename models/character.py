from odoo import models, fields, api


class Character(models.Model):
    #Special fields
    _name = 'character'
    _description = 'Characters in the game'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Character\'s name'
    )

    c_class = fields.Selection(
        string='Class',
        selection=[('Barbarian', 'barbarian'), ('Bard', 'bard'), ('Cleric', 'cleric'), ('Druid', 'druid')]
    )
    
    exp = fields.Integer(
        string='Experience',
    )
    
    level = fields.Integer(
        compute='_compute_level', 
        store=True  
    )
    
    race = fields.Selection(
        string='Race',
        selection=[('valor1', 'valor1'), ('valor2', 'valor2')]
    )
    
    strength = fields.Char(
        string='Strength',
        size=255,
    )
    
    dexterity = fields.Char(
        string='Dexterity',
        size=255
    )
    
    constitution = fields.Char(
        string='Constitution',
        size=255,
    )
    
    intelligence = fields.Char(
        string='Intelligence',
        size=255,
    )
    
    wisdom = fields.Char(
        string='Wisdom',
        size=255
    )
    
    charisma = fields.Char(
        string='Charisma',
        size=255
    )

    spell_slots_ids = fields.One2many(
        string='Spell slots',
        comodel_name='spell_slot',
        inverse_name='character_id',
    )

    items_ids = fields.Many2many(
        string='Items',
        comodel_name='item',
        relation='item_character_rel',
        column1='item_id',
        column2='character_id',
    )
    
    spells_known_ids = fields.Many2many(
        string='Spells known',
        comodel_name='spell',
        relation='spell_know_character_rel',
        column1='spell_id',
        column2='character_id',
    )
    
    spells_prepared_ids = fields.Many2many(
        string='Spells prepared',
        comodel_name='spell',
        relation='spell_prepared_character_rel',
        column1='spell_id',
        column2='character_id',
    )
    
    max_hp = fields.Integer(
        string='Max hp',
    )
    
    hp = fields.Integer(
        string='Hp',
    )
    
    necrotic_dmg = fields.Integer(
        string='necrotic_dmg',
    )
    
    money = fields.Integer(
        string='Money',
    )
    
    img = fields.Binary(
        string='Image',
    )