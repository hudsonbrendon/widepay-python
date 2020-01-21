from decouple import config

from widepay import WidePay


if __name__ == "__main__":
    widepay = WidePay(id=config("ID"), token=config("TOKEN"))
    carne = widepay.gerar_carne(
        cliente="Hudson Brendon",
        pessoa="Física",
        cpf="789.830.400-41",
        vencimento="2020-12-12",
        parcelas=10,
        dividir="Não",
        itens=[{"descricao": "Descrição item 1", "valor": 20,}],
    )
    print(carne)
