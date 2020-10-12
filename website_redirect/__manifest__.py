{
    "name": "Website Redirect",
    "summary": "Set the absolute base URL on a relative redirect to the website domain",
    "category": "Website",
    "version": "13.0.1.0.0",
    "author": "Agrista GmbH,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["base", "website"],
    "data": [
        'views/website_views.xml',
        'views/res_config_settings_views.xml',
    ],
    "installable": True,
}
