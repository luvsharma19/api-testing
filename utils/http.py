import requests
from utils.configuration import Configuration


class Http:
    config = Configuration.global_config['server']
    host = config['host']
    port = config['port']
    restUri = config['restUri']
    uri = host + ':' + port + restUri
    timeout = 3

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    @staticmethod
    def getResult(response):
        return {
            'data': response.json(),
            'status_code': response.status_code
        }

    def setHeaders(self, custom_header={}):
        for key in custom_header.keys():
            self.headers[key] = custom_header[key]

    def get(self, resource):
        response = requests.get(self.uri + resource, headers=self.headers,
                                timeout=self.timeout, verify=False)
        return self.getResult(response)

    def post(self, resource, reqBody):
        response = requests.post(self.uri + resource, headers=self.headers,
                                 timeout=self.timeout, json=reqBody,
                                 verify=False)
        return self.getResult(response)

    def put(self, resource, reqBody={}):
        response = requests.put(self.uri+resource, json=reqBody,
                                headers=self.headers, timeout=self.timeout,
                                verify=False)
        return self.getResult(response)

    def delete(self, resource):
        response = requests.delete(self.uri+resource, headers=self.headers,
                                   timeout=self.timeout, verify=False)
        return {
            'status_code': response.status_code
        }
