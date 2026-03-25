from odoo import http
from odoo.http import route, request

from werkzeug.utils import redirect

class ShortLinkController(http.Controller):
    @route(
        "/sl/<string:shortlink>",
        type="http",
        auth="public",
    )
    def redirect(self, shortlink):

        shortlink_model = request.env['tli.shortlink'].sudo().search(
            [('key', '=', shortlink)]
        )
        
        if not shortlink_model:
            return redirect('/404.html', code=404)

        redirect_url, code = shortlink_model.get_url()
        
        return redirect(
            redirect_url,
            code=code
        )
