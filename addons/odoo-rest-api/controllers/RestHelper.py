from odoo import _
from odoo.http import Response


class RestHelper:

    @staticmethod
    def JsonValidResponse(data, valid_code=200):
        """
        Return a JsonResponse with the given data and status code if code is valid or no exceptions.
        """
        Response.status = str(valid_code)
        return {
            'status_code': valid_code,
            'message': _('success'),
            'data': data,
            'success': True
        }

    @staticmethod
    def JsonErrorResponse(error, error_code=400):
        """
        Return a JsonResponse with the given data and status code if code is not valid or with exceptions.
        """
        Response.status = str(error_code)
        return {
            'code': error_code,
            'message': _('failed'),
            'error': error,
            'success': False
        }
