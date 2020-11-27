# coding: utf-8

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def get_base_url(self):
        self.ensure_one()
        url = ''
        website = self.website_id
        if not website and self.company_id:
            website = self.env['website'].search(
                [('company_id', '=', self.company_id.id)], limit=1)
        if website:
            url = website._get_http_redirect_domain(
            ) if website.redirect_domain else website._get_http_domain()
        return url or super(ResPartner, self).get_base_url()
