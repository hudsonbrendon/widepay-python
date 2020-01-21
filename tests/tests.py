import unittest
import requests_mock

from decouple import config
from widepay import WidePay
from requests.auth import HTTPBasicAuth


class TestWidePay(unittest.TestCase):
    def setUp(self):
        self.widepay = WidePay(id=config("ID"), token=config("TOKEN"))

    def test_get_url(self):
        self.assertEqual(self.widepay._get_url("/test"), f"{self.widepay._URL}/test")

    def test_authentication(self):
        self.assertEqual(
            self.widepay.authentication(),
            HTTPBasicAuth(self.widepay.id, self.widepay.token),
        )

    @requests_mock.Mocker()
    def test_gerar_carne(self, request_mock):
        url = self.widepay._get_url(path="/recebimentos/carnes/adicionar")
        json = {
            "sucesso": True,
            "id": "1",
            "link": "https://www.widepay.com/carne/425692-1",
            "pdf": "https://www.widepay.com/carne/425692-1.pdf",
            "cobrancas": [
                "24940A1F79B30E65",
                "9D83FF1579B30E6F",
                "59793B1579BD046F",
                "12385A1F79B3A46F",
                "5FF869B579B3AE65",
                "42C286B57913046F",
                "39770BBF7913A46F",
                "85E93FB57913A46F",
                "9EE5C1B5791DAE6F",
                "6A56261F79130E66",
            ],
        }
        request_mock.post(url=url, json=json)
        carne = self.widepay.gerar_carne(
            cliente="Hudson Brendon",
            pessoa="Física",
            cpf="789.830.400-41",
            vencimento="2020-12-12",
            parcelas=10,
            dividir="Não",
            itens=[{"descricao": "Descrição item 1", "valor": 20,}],
        )
        self.assertEqual(carne, json)


if __name__ == "__main__":
    unittest.main()
