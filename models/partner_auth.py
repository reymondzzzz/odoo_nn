from odoo import fields, models


class PartnerAuth(models.Model):
    _name = "nn.partner.auth"
    _description = "Partner Authentication"
    _rec_name = "partner_id"

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        required=True,
        ondelete="cascade",
        index=True,
    )
    password_hash = fields.Char(
        string="Password Hash",
        help="Bcrypt password hash for booking portal authentication",
    )
    auth_provider = fields.Selection(
        selection=[
            ("credentials", "Email/Password"),
            ("google", "Google"),
        ],
        string="Auth Provider",
        help="Authentication provider used by this customer",
    )
    provider_id = fields.Char(
        string="Provider ID",
        help="OAuth provider user ID (Google, Facebook, etc.)",
        index=True,
    )

    _sql_constraints = [
        ("partner_uniq", "unique(partner_id)", "Each partner can only have one auth record"),
        ("provider_id_uniq", "unique(auth_provider, provider_id)", "Provider ID must be unique per provider"),
    ]
