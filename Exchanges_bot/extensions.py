import requests
import json
from config import exchanges


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')
        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f'Валюта {sym} не найдена!')

        if base_key == sym_key:
            raise APIException(f'Невозможно провести одинаковые валюты {base}!')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количетсво {amount}!')

        response = requests.get(f'https://api.apilayer.com/exchangerates_data/latest?symbols={sym_key}&base={base_key}',
                                headers={
                                    "apikey": "a4kta3YDI5dKfV3QQdk4vM5lfxN4bipG"
                                })
        resp = json.loads(response.content)
        new_price = resp['rates'][sym_key] * float(amount)
        result = round(new_price, 3)
        return result
