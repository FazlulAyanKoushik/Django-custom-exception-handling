from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotAuthenticated, PermissionDenied
from django.http import Http404


def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # Define a dictionary to map exception classes to handler functions
    handler = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
    }

    # Get the exception class name
    exception_class = exc.__class__.__name__

    if response is not None:
        # Here ProductList is the view name and checking is it in the context and response status code is 401
        # if "ProductList" in str(context['view']) and response.status_code == 401:
        #     response.status_code = 200
        #     response.data = {
        #         "is_logged_in": False,
        #         "status_code": response.status_code,
        #     }
        #
        #     return response
        # import pdb
        # pdb.set_trace()
        response.data['status_code'] = response.status_code

    # If the exception is recognized, use the appropriate handler
    if exception_class in handler:
        return handler[exception_class](exc, context, response)

    return response


def _handle_generic_error(exc, context, response):
    # Customize the response for generic errors
    response.data = {
        'error': str(exc),
        'status_code': response.status_code,
    }
    return response


def _handle_authentication_error(exc, context, response):
    # Customize the response for authentication errors
    response.data = {
        'error': 'Authentication credentials were not provided.',
        "status_code": response.status_code,
    }
    return response
