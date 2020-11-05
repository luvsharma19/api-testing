import pytest
from helper.authentication import Authentication
from utils.http import Http


@pytest.fixture(scope='class', autouse=True)
def authenticate(request):
    token = Authentication.get_authtoken()
    request.cls.token = token
    yield token
    Authentication.delete_authtoken(token)

@pytest.fixture(scope='class', autouse=True)
def http_object(request):
    token = request.cls.token
    http_object = Http()
    http_object.setHeaders({'Authorization': token})
    return http_object
