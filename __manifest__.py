{
    'name': 'Library Management',
    'version': '1.0.0',
    'sequence': -100,

    'depends': ['base'],
    'data': [
        'security/library_book_security.xml',
        'security/ir.model.access.csv',
        'views/library_author_view.xml',
        'views/library_book_view.xml',
        'views/library_publisher_view.xml',
        'views/library_genre_view.xml',
        'views/library_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'library/static/src/js/new_book_validation.js',
        ],

    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
