# -*- coding: utf-8 -*-
{
    'name': "codev2",

    'summary': """编码管理""",

    'description': """编码管理""",

    'author': "ZHY",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'data/resistance_rules_sequence.xml',
        'views/manager.xml',
    ],
    # 'css': [
    #     'static/src/css/codev2.css'
    # ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}