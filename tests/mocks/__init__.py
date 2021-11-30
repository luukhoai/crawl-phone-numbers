from requests.exceptions import RequestException
from marshmallow.exceptions import MarshmallowError


class MockResponse(object):

    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


def _mock_get_place():
    return MockResponse({
        'candidates': [
            {'place_id': 'ChIJm7NJkla3j4AR8vR-HWRxgOo'},
            {'place_id': 'ReYdBhOQN2UoVDhS12G-OjfgUei'}],
        'status': 'OK'
    })


def _mock_get_phone():
    return MockResponse({
        'html_attributions': [],
        'result': {'formatted_phone_number': '(650) 810-1010'},
        'status': 'OK'
    })


def _mock_get_zero_results():
    return MockResponse({
        'status': 'ZERO_RESULTS'
    })


def _mock_get_invalid_request():
    return MockResponse({
        'status': 'INVALID_REQUEST'
    })


def _mock_get_not_found():
    return MockResponse({
        'status': 'NOT_FOUND'
    })


def _mock_internal_error():
    return MockResponse({
        'status': 'UNKNOWN_ERROR'
    })


def _mock_raise_request_exception():
    raise RequestException('Exception')


def mock_raise_marshmallow_exeption(*args):
    raise MarshmallowError('Exception')


def _mock_url(*args, place, detail):
    url = args[0]
    if 'findplacefromtext' in url:
        return place()
    else:
        return detail()


def mock_get_place_success(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_get_phone)


def mock_get_place_zero_result(*args):
    return _mock_url(*args, place=_mock_get_zero_results, detail=_mock_get_phone)


def mock_get_place_invalid(*args):
    return _mock_url(*args, place=_mock_get_invalid_request, detail=_mock_get_phone)


def mock_get_place_internal(*args):
    return _mock_url(*args, place=_mock_internal_error, detail=_mock_get_phone)


def mock_get_place_raise_exception(*args):
    return _mock_url(*args, place=_mock_raise_request_exception, detail=_mock_get_phone)


def mock_get_detail_zero_result(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_get_zero_results)


def mock_get_detail_not_found(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_get_not_found)


def mock_get_detail_invalid(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_get_invalid_request)


def mock_get_detail_internal(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_internal_error)


def mock_get_detail_raise_exception(*args):
    return _mock_url(*args, place=_mock_get_place, detail=_mock_raise_request_exception)
