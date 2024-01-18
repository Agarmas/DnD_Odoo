from odoo import models, fields, api

class Character(models.Model):
    # Special fields
    _name = 'character'
    _description = 'Characters in the game'

    # Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Character\'s name'
    )
    
    c_classes_ids = fields.Many2many(
        string='Classes',
        comodel_name='c_class',
        relation='c_class_character_rel',
        column1='c_class_id',
        column2='character_id',
    )
    
    exp = fields.Integer(
        string='Experience',
    )
    
    level = fields.Integer(
        string='Level',        
        compute='_compute_level', 
        store=True  
    )
    
    race_id = fields.Many2one(
        string='Race',
        comodel_name='race',
        ondelete='restrict',
    )
    
    languages_ids = fields.Many2many(
        string='languages',
        comodel_name='language',
        relation='language_character_rel',
        column1='language_id',
        column2='character_id',
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
        string='Necrotic damage',
    )
    
    money = fields.Integer(
        string='Money',
    )
    
    img = fields.Binary(
        string='Image',
    )
    
    alingment = fields.Selection(
        string='Alingment',
        selection=[('CE', 'Chaotic-Evil'), ('CN', 'Chaotic-Neutral'), ('CG', 'Chaotic-Good'), ('NE', 'Neutral-Evil'), ('NN', 'Neutral-Neutral'), ('NG', 'Neutral-Good'), ('LE', 'Lawful-Evil'), ('LN', 'Lawful-Neutral'), ('LG', 'Lawful-Good')]
    )
    
    inspiration = fields.Boolean(
        string='Inspiration',
    )
    
    armor_class = fields.Integer(
        string='Armor class',
    )
    
    proficency_bonus = fields.Integer(
        string='Proficency bonus',
        compute='_compute_proficency_bonus',
        store=True
    )
    
    initiative = fields.Integer(
        string='Initiative',
    )
    
    speed = fields.Integer(
        string='Speed',
        help='Ft'
    )
    
    age = fields.Integer(
        string='Age',
    )
    
    height = fields.Integer(
        string='Height',
        help='cm'
    )
    
    weight = fields.Float(
        string='Weight',
        help='Kg'
    )
    
    lore = fields.Text(
        string='Lore',
    )

    # Computed 
    @api.depends('exp')
    def _compute_level(self):
        for character in self:
            if character.exp < 300:
                character.level = 1
            elif character.exp < 900:
                character.level = 2
            elif character.exp < 2700:
                character.level = 3
            elif character.exp < 6500:
                character.level = 4
            elif character.exp < 14000:
                character.level = 5
            elif character.exp < 23000:
                character.level = 6
            elif character.exp < 34000:
                character.level = 7
            elif character.exp < 48000:
                character.level = 8
            elif character.exp < 64000:
                character.level = 9
            elif character.exp < 85000:
                character.level = 10
            elif character.exp < 100000:
                character.level = 11
            elif character.exp < 120000:
                character.level = 12
            elif character.exp < 140000:
                character.level = 13
            elif character.exp < 165000:
                character.level = 14
            elif character.exp < 195000:
                character.level = 15
            elif character.exp < 225000:
                character.level = 16
            elif character.exp < 265000:
                character.level = 17
            elif character.exp < 305000:
                character.level = 18
            elif character.exp < 355000:
                character.level = 19
            else:
                character.level = 20

    @api.depends('level')
    def _compute_proficency_bonus(self):
            for character in self:
                if character.level > 0:
                    character.proficency_bonus = (character.level - 1) / 4 + 2
                    if character.proficency_bonus < 1:
                        character.proficency_bonus = 1
                else:
                    character.proficency_bonus = 0