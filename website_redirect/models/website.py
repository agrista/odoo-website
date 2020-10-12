# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    redirect_domain = fields.Char(
        'Redirect Domain',
        help='Redirects to this domain for relative redirects')
