# -*- coding: utf-8 -*-
{
    'name': 'HR Report',
    'summary': """
        HR Report
    """,
    'license' : 'OPL-1',
    'version': '1.1',
    'author': 'Anand Rudani',
    'description': """
        HR Report
    """,
    'depends' : ['hr'],
    'data': [
        'views/report.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'hr_report_customize/static/src/scss/report.scss',
        ],
    },
    'images': [],
    'installable': True,
    'application': True,
}
