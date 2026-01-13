from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_password_hash = fields.Char(
        string="Password Hash",
        help="Bcrypt password hash for booking portal authentication",
    )
    x_auth_provider = fields.Selection(
        selection=[
            ("credentials", "Email/Password"),
            ("google", "Google"),
        ],
        string="Auth Provider",
        help="Authentication provider used by this customer",
    )
    x_provider_id = fields.Char(
        string="Provider ID",
        help="OAuth provider user ID (Google, Facebook, etc.)",
        index=True,
    )
