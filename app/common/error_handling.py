from http import HTTPStatus


def handle_validation_error(e):
    data = {
        'errorType': 'ValidationError',
        'errors': e.description
    }
    return data, HTTPStatus.BAD_REQUEST


def handle_internal_error(e):
    data = {
        'errorType': 'InternalError',
        'errors': e.description
    }
    return data, HTTPStatus.INTERNAL_SERVER_ERROR
