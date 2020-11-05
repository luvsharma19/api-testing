from utils.configuration import Configuration
import json


class TestUser:
    user_id = ''
    token = ''
    resource = Configuration.global_config['resources']['users']
    with open('tests/user/input.json') as inputFile:
        input = json.load(inputFile)

    def test_create_user(cls, authenticate, http_object):
        result = http_object.post(cls.resource, cls.input['requestBody'])
        cls.user_id = result['data']['id']
        assert result['status_code'] == 200

    def test_edit_user(cls, authenticate, http_object):
        resource = cls.resource + '/' + cls.user_id
        req_body = cls.input['requestBody']
        req_body['name'] = "Kush"
        print(req_body)
        result = http_object.put(resource, req_body)
        assert result['status_code'] == 202

    def test_delete_user(cls, authenticate, http_object):
        resource = cls.resource + '/' + cls.user_id
        result = http_object.delete(resource)
        assert result['status_code'] == 200
