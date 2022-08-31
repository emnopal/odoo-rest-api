from odoo import http, _
from .RestHelper import RestHelper
from typing import Dict


class RestCheck(http.Controller):

    """
    Checking if REST API is active, and also checking for available database
    """

    @http.route([
        '/api/ping',
        '/api/check/health',
        '/api/check',
        '/api/health',
    ], auth="public", type="json", csrf=False
    )
    def CheckServer(self) -> Dict[str, any]:
        """
        Checking the server
        """
        try:
            return RestHelper.JsonValidResponse(_('Okay'))
        except Exception as e:
            return RestHelper.JsonErrorResponse(_(e))

    @http.route([
        '/api/db',
        '/api/database'
    ], auth="public", type="json", csrf=False
    )
    def DBList(self) -> Dict[str, any]:
        """
        List of Available Database
        """
        try:
            return RestHelper.JsonValidResponse(http.db_list())
        except Exception as e:
            return RestHelper.JsonErrorResponse(_(e))
