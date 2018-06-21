# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",


    'author': "O-SIAT",
    'website': "http://www.o-sait.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        '/opt/odoo/my-modules/openacademy/demo/openacademy_course_demo.xml',
    ],
    'installable':True,
    'auto_install':False,
}

