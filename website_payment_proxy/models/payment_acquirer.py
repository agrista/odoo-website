# coding: utf-8

from odoo import models


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    def get_base_url(self):
        self.ensure_one()
        # priority is always given to url_root
        # from the request
        url = ''
        if 'website_id' in self and self.website_id:
            url = self.website_id._get_http_domain()
        return url or super(PaymentAcquirer, self).get_base_url()
