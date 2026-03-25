{
    'name': "Short Links",
    'summary': """
    Shortlink creation.
    """,
    'description': """
        App to redirect from a long URL toward a shortlink.
        Can create links to redirect to internal or external URL.
    """,
    'author': "TheLastImperial",
    'website': 'https://github.com/TheLastImperial/tli_shortlink',
    'category': 'TheLastImperial/Shortlink',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'base'
    ],
    'application': True,
    'installable': True,
    'data': [
        'security/security.xml',
        'views/shortlink_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
    ],
}
