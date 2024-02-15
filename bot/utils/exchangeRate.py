import requests


def currency_converter(amount: float, currency_from: str, currency_to: str) -> float:
    """Конвертирует валюты: currency_from = 'USD', currency_to = 'EUR', amount = 100"""
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{currency_from}')
    data = response.json()
    exchange_rate = float(data['rates'][currency_to])
    result = amount * exchange_rate
    result = round(result, 2)
    return result


