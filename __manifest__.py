{
    'name': "Dungeons And Dragons",

    'summary': """DnD 5e assistance""",

    'description': """Manage DnD 5e player game""",

    'author': "Antonio Garrido Massé",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Games',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/items_view.xml',
        'views/spells_view.xml',
        'views/spell_slots_view.xml',
        'views/characters_view.xml',
        'views/menu.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [   
        'demo/items_demo.csv',
        'demo/spells_demo.csv',
    ],
    
    'installable': True,
    'application': True,
}