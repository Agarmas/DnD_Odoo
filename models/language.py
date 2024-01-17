from odoo import models, fields, api

class Language(models.Model):
     #Special fields
    _name = 'language'
    _description = 'Characters in the game'

    #Fields
    name = fields.Char(
        string='Name',
        size=255
    )
   