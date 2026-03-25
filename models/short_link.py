import shortuuid

from odoo import api, fields, models
from odoo.exceptions import ValidationError
# from werkzeug.exceptions import NotFound

class ShortLink(models.Model):
    _name = 'tli.shortlink'
    _description = """
        Shortlink model.
    """
    name = fields.Char(required=True)
    description = fields.Char()
    url = fields.Char(required=True)
    key = fields.Char()

    sl = fields.Char(
        compute='_compute_shortlink'
    )
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    _check_unique_key = models.Constraint(
        "UNIQUE(key)", "The key must be unique"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for shortlink in vals_list:
            # Validate valid URL
            if shortlink["url"][:8] != "https://":
                raise ValidationError(
                    Exception("The URL must init with 'https://'.")
                )
            # Set a Unit key
            key = shortuuid.ShortUUID().random(length=6)
            while(self.exist_key(key)):
                key = shortuuid.ShortUUID().random(length=6)
            shortlink["key"] = key

        shortlinks = super().create(vals_list)
        return shortlinks

    def _compute_shortlink(self):
        for record in self:
            if record.id:
                base_url = self.env[
                    'ir.config_parameter'
                ].sudo().get_param('web.base.url')
                record.sl = base_url + "/sl/" + record.key
            else:
                record.sl = ""

    def exist_key(self, key_val):
        record = self.env['tli.shortlink'].search(
            [('key', '=', key_val)]
        )
        return record.exists()

    def get_url(self):
        can_pass = self.active

        redirect_url = None
        code = 404

        if can_pass:
            redirect_url = self.url
            code = 302
        else:
            redirect_url = self.env[
                'ir.config_parameter'
            ].sudo().get_param('web.base.url')

            redirect_url += "/404.html"

        return redirect_url, code
