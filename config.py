import requests

TOKEN = '6081271530:AAG3HLfJVIZ-tFehtEdNL50F_UdNxkDt74Y'

courses = {
    'USD': 0,
    'EUR': 0,
    'RUB': 0
}

# proxies = {
#     'https': 'https://52.183.8.192:3128'
# }

response_uzs = requests.get('https://v6.exchangerate-api.com/v6/996a84d6ad5bf8b94d0960af/latest/UZS')
response_usd = requests.get('https://v6.exchangerate-api.com/v6/996a84d6ad5bf8b94d0960af/latest/USD')
response_rub = requests.get('https://v6.exchangerate-api.com/v6/996a84d6ad5bf8b94d0960af/latest/RUB')
response_eur = requests.get('https://v6.exchangerate-api.com/v6/996a84d6ad5bf8b94d0960af/latest/EUR')
