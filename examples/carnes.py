from decouple import config

from widepay import WidePay


if __name__ == '__main__':
    widepay = WidePay(id=config('ID'), token=config('TOKEN'))
    carne = widepay.gerar_carne(
        cliente='Cliente de teste',
        pessoa='Física',
        vencimento='2020-12-12'
    )
    print(carne)