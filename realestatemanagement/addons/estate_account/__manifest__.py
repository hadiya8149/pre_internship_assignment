{

  'name': "Real-Estate Management Accounts",

  'version': '1.0',

  'depends': ['base'],

  'author': "Hadiya   Asif",

  'category': 'Category',

  'description': """

  This is a test module of Real-Estate Management!

  Written for the Odoo Quickstart Tutorial.

  """,

  # data files always loaded at installation

  'data': [


  ],
'depends': [  'base','estate','account' ],

  'installable': True,

  'auto_install': False,

  'application': False,

}