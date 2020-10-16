# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from werkzeug import urls

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    redirect_domain = fields.Char(
        'Redirect Domain',
        help='Redirects to this domain for relative redirects')

    def _get_http_redirect_domain(self):
        self.ensure_one()
        if not self.redirect_domain:
            return ''
        res = urls.url_parse(self.redirect_domain)
        return 'http://' + self.redirect_domain if not res.scheme else self.redirect_domain
