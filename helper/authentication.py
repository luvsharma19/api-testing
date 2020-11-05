from utils.http import Http
from utils.configuration import Configuration


class Authentication:
    http_object = Http()
    config = Configuration.global_config['user_credentials']
    username = config['username']
    password = config['password']

    @classmethod
    def get_authtoken(cls):
        req_body = {
          'user': cls.username,
          'password': cls.password
        }
        response = cls.http_object.post('credentials', req_body)
        data = response['data']
        return data['token']

    @classmethod
    def delete_authtoken(cls, token):
        resource = 'credentials/' + token
        cls.http_object.delete(resource)


