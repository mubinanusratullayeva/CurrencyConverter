import requests

TOKEN = '6081271530:AAG3HLfJVIZ-tFehtEdNL50F_UdNxkDt74Y'

courses = {
    'USD': 0,
    'EUR': 0,
    'RUB': 0
}

response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')