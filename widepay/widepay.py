import requests

from requests.auth import HTTPBasicAuth


class WidePay(object):

    _URL = 'https://api.widepay.com/v1'

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def _get_url(self, path):
        return f'{self._URL}{path}'

    def _request(self, url, method, data=None):
        if method.lower() == 'get':
            request = requests.get(url, auth=self.authentication())
        elif method.lower() == 'post':
            request = requests.post(url, data=data, auth=self.authentication())
        elif method.lower() == 'put':
            request = requests.put(url, data=data, auth=self.authentication())
        elif method.lower() == 'delete':
            request = requests.delete(url, auth=self.authentication())
        else:
            pass
        return request.json()

