# -*- coding: utf-8 -*-
{
    'name': "Company Logo",
    'summary': """Company logo inside invoice report header""",
    'description': """Logo""",
    'author': "Abdul Halim",
    'website': "https://abdulhalim.pythonanywhere.com",
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'report', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_invoice.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
