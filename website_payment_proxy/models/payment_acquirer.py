# coding: utf-8

from odoo import models


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    def get_base_url(self):
        self.ensure_one()
        url = ''
        if 'website_id' in self and self.website_id:
            url = self.website_id._get_http_redirect_domain(
            ) if self.website_id.redirect_domain else self.website_id._get_http_domain(
            )
        return url or super(PaymentAcquirer, self).get_base_url()
