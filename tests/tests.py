import unittest

from decouple import config
from widepay import WidePay
from requests.auth import HTTPBasicAuth


class TestWidePay(unittest.TestCase):

    def setUp(self):
        self.widepay = WidePay(id=config('ID'), token=config('TOKEN'))

    def test_get_url(self):
        self.assertEqual(self.widepay._get_url('/test'), f'{self.widepay._URL}/test')

    def test_authentication(self):
        self.assertEqual(self.widepay.authentication(), HTTPBasicAuth(self.widepay.id, self.widepay.token))


if __name__ == '__main__':
    unittest.main()