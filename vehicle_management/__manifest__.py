{
    'name': 'vehicle_management',
    'summary': 'Manage Vehicle Brands and Models',
    'category': 'Management',
    'author': 'Your Name',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_brand_views.xml',
        'views/vehicle_model_views.xml',
        'views/vehicle_master_views.xml',
        'views/vehicle_management_menu.xml',
        # 'views/sale_order_views.xml'
        'wizard/vehicle_wizard_views.xml',

    ],
    'installable': True,
    'application': True,
}
