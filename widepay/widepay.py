import requests

from requests.auth import HTTPBasicAuth


class WidePay(object):

    _URL = "https://api.widepay.com/v1/"

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def _get_url(self, path):
        return f"{self._URL}{path}"
    
    @property
    def authentication(self):
        return HTTPBasicAuth(self.id, self.token)

    def _request(self, method, path, json, **kwargs):
        request = requests.request(
            method=method,
            url=self._get_url(path),
            auth=self.authentication,
            json=json,
            **kwargs,
        )
        json = request.json()

        return json

    def gerar_carne(
        self,
        cliente,
        pessoa,
        itens,
        vencimento,
        parcelas,
        dividir,
        cpf=None,
        cnpj=None,
        email=None,
        telefone=None,
        endereco=None,
        referencia=None,
        notificacao=None,
        enviar=None,
        mensagem=None,
        marketplace=None,
        boleto=None,
    ):
        """
        Um carnê é formado por várias cobranças agrupadas, as parcelas de um
        carnê tem o vencimento mensal, por exemplo, ao gerar um carnê com o primeiro
        vencimento para 15/03, a próxima parcela terá o vencimento para 15/04, sempre com intervalo de 1 mês.

        Saiba mais em:

        https://widepay.github.io/api/index.html#carnes
        """
        path = "recebimentos/carnes/adicionar"

        json = {
            "cliente": cliente,
            "pessoa": pessoa,
            "itens": itens,
            "vencimento": vencimento,
            "parcelas": parcelas,
            "dividir": dividir,
            "cpf": cpf,
            "cnpj": cnpj,
            "email": email,
            "telefone": telefone,
            "endereco": endereco,
            "referencia": referencia,
            "notificacao": notificacao,
            "enviar": enviar,
            "mensagem": mensagem,
            "marketplace": marketplace,
            "boleto": boleto,
        }

        request = self._request(method="post", path=path, json=json)

        return request

    def gerar_cobranca(self, forma, cliente, pessoa, itens, vencimento, cpf=None, cnpj=None, email=None, endereco=None, referencia=None, notificacao=None, redirecionamento=None, enviar=None, mensagem=None, marketplace=None, boleto=None):
        """
        Em cobranças, você pode realizar recebimentos via boleto ou cartão de crédito.
        Confira na tabela abaixo a lista de todos os status de uma cobrança e sua respectiva descrição.

        Saiba mais em:

        https://widepay.github.io/api/#cobranca-gerando
        """
        path = "recebimentos/cobrancas/adicionar"

        json = {
            "forma": forma,
            "cliente": cliente,
            "pessoa": pessoa,
            "itens": itens,
            "vencimento": vencimento,
            "cpf": cpf,
            "cnpj": cnpj,
            "email": email,
            "endereco": endereco,
            "referencia": referencia,
            "notificacao": notificacao,
            "redirecionamento": redirecionamento,
            "enviar": enviar,
            "mensagem": mensagem,
            "marketplace": marketplace,
            "boleto": boleto
        }

        request = self._request(method="post", path=path, json=json)

        return request