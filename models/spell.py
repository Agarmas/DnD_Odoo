from odoo import models, fields, api


class Spell(models.Model):
    #Special fields
    _name = 'spell'
    _description = 'Posible spells in the game'

    #Fields
    name = fields.Char(
        string='Name',
        size=255,
        required=True,
        help='Spell\'s name'
    )

    classes = fields.Char(
        string='Classes', 
        size=255, 
        help='Spell\'s classes'
    )

    level = fields.Integer(
        string='Level',
        help='Spell\'s level'
    )

    
    school = fields.Char(
        string='School',
        help='Spell\'s magic school'
    )

    cast_time = fields.Char(
        string='Cast time',
        help='Spell\'s cast time'
    )

    range = fields.Char(
        string='Range',
        help='Spell\'s range'
    )

    duration = fields.Char(
        string='Duration',
        help='Spell\'s duration'
    )

    verbal = fields.Boolean(
        string='Verbal',
    )

    somatic = fields.Boolean(
        string='Somatic',
    )

    material = fields.Boolean(
        string='Material',
    )

    ritual = fields.Boolean(
        string='Ritual',
    )

    material_cost = fields.Char(
        string='Material cost',
        help='Spell\'s material cost'
    )

    description = fields.Text(
        string='Description',
        help='Spell\'s description'
    )
          