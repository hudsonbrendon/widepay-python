from decouple import config

from widepay import WidePay


if __name__ == "__main__":
    widepay = WidePay(id=config("ID"), token=config("TOKEN"))
    cobranca = widepay.gerar_cobranca(
        forma="Cartão",
        cliente="Hudson Brendon",
        pessoa="Física",
        cpf="789.830.400-41",
        vencimento="2020-10-10",
        itens=[{"descricao": "Descrição item 1", "valor": 20}],
    )
    print(cobranca)
