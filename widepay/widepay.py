import requests

from requests.auth import HTTPBasicAuth


class WidePay(object):

    _URL = 'https://api.widepay.com/v1'

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def _get_url(self, path):
        return f'{self._URL}{path}'
