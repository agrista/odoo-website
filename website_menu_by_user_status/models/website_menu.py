# Copyright 2013-2017 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WebsiteMenu(models.Model):
    """Improve website.menu with adding booleans that drive
    if the menu is displayed when the user is logger or not.
    """

    _inherit = 'website.menu'

    user_logged_in = fields.Boolean(
        string="User Logged In",
        default=True,
        help=_("If checked, "
               "the menu will be displayed when the user is logged in "
               "and given access.")
    )

    user_not_logged_in = fields.Boolean(
        string="User Not Logged In",
        default=True,
        help=_("If checked, "
               "the menu will be displayed when the user is not logged "
               "and give access.")
    )

    def _compute_visible(self):
        """Display the menu item whether the user is logged or not."""
        super()._compute_visible()
        for menu in self:
            if not menu.is_visible:
                return

            if menu.env.user == menu.env.ref('base.public_user'):
                menu.is_visible = menu.user_not_logged_in
            else:
                menu.is_visible = menu.user_logged_in
