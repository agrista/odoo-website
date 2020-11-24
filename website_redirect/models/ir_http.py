from werkzeug import urls

import odoo
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = ['ir.http']

    @classmethod
    def _get_website_domain(cls):
        domain = ''
        if hasattr(request, 'website') and request.website.redirect_domain:
            domain = request.website.redirect_domain
        elif hasattr(request, 'website_routing'):
            website = request.env['website'].get_current_website()
            domain = website.redirect_domain or ''
        if domain:
            parsed_url = urls.url_parse(domain)
            if not parsed_url.scheme:
                domain = 'http://' + domain
        return domain

    @classmethod
    def _dispatch(cls):
        result = super(IrHttp, cls)._dispatch()
        if hasattr(result, 'location'
                   ) and result.location and result.location.startswith('/'):
            result.location = cls._get_website_domain() + result.location
        return result
