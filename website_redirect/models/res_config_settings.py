# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    website_redirect_domain = fields.Char('Redirect Domain', related='website_id.redirect_domain', readonly=False)
