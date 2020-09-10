# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug import urls

from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class Website(models.Model):
    _inherit = "website"

    @api.constrains('domain')
    def _check_domain(self):
        if not self.domain:
            return
        res = urls.url_parse(self.domain)
        if not res.scheme:
            raise ValidationError(_("Domain needs a protocol e.g. 'https://'"))
