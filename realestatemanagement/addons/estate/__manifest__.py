{

  'name': "Real-Estate Management",

  'version': '1.0',

  'depends': ['base'],

  'author': "Hadiya  skdlf Asif",

  'category': 'Category',

  'description': """

  This is a test module of Real-Estate Management!

  Written for the Odoo Quickstart Tutorial.

  """,

  # data files always loaded at installation

  'data': [
    'security/ir.model.access.csv',

    'views/estate_property_offers.xml',
          'views/estate_property_type.xml',
          'views/estate_property_tags.xml',
      'views/estate_property_views.xml',
      'views/res_users_views.xml',
    'data/property_tags.xml',
    'data/estate.xml',
    'data/estate_property_type.xml',
    'data/estate_property_offer.xml',

  ],
'depends': [  'base' ],

  'installable': True,

  'auto_install': False,

  'application': False,

}