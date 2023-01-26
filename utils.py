import json
import requests
from config import*
from app import*

class ConvertionExсeption(Exception):
    pass

class CryptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExсeption(
                f'Вы переводите валюту {base} в валюту в такую же. Совсем что ли?\nВалюты должны быть разные!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExсeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExсeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExсeption(f'Не удалось обработать количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')



