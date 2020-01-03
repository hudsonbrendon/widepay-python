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

    def authentication(self):
        return HTTPBasicAuth(self.id, self.token)

    def gerar_carne(self):
        """
        Um carnê é formado por várias cobranças agrupadas, as parcelas de um
        carnê tem o vencimento mensal, por exemplo, ao gerar um carnê com o primeiro
        vencimento para 15/03, a próxima parcela terá o vencimento para 15/04, sempre com intervalo de 1 mês.

        Saiba mais em:

        https://widepay.github.io/api/index.html#carnes
        """
        url = self._get_url(path='/recebimentos/carnes/adicionar')

        data = dict(
            cliente='Maria Mayse',
            pessoa='Física',
            vencimento='2020-10-10',
            cpf='463.384.662-02',
            dividir='Não',
            parcelas=6,
            itens=[
                dict(
                    descricao='Descrição item 1',
                    valor=22.50
                )
            ]
        )

        request = self._request(url=url, method='post', data=data)

        return request
