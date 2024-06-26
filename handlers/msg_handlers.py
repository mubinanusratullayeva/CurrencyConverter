import requests
from aiogram.types import Message
from aiogram import Router

from config import response_usd

msg_router = Router()


data_usd = response_usd.json()


@msg_router.message()
async def convert_dollar(message: Message):
    try:
        foo = int(message.text)

        txt = ""
        for course in data_usd['conversion_rates']:
            if course in ['EUR', 'RUB', 'UZS']:
                txt += f"{foo} dollar = {foo * data_usd['conversion_rates'][course]:.2f} {course}\n"

        await message.reply(text=txt)
    except ValueError:
        await message.reply("Please enter a valid number.")
