import requests
from aiogram.types import Message
from aiogram import Router

from config import courses, response

msg_router = Router()

print(response)

@msg_router.message()
async def convert_dollar(message: Message):

    for course in response.json():
        try:
            foo = int(message.text)
            if course['Ccy'] in ['EUR', 'RUB']:
                txt = f"{foo} dollar: \n"
                txt += f"{foo * course['Rate']: .2f} sum\n"
                txt += f"{foo * courses[course['EUR']]: .2f} euro\n"
                txt += f"{foo * courses[course['RUB']]: .2f} ruble\n"
                await message.reply(text=txt)
        except:
            await message.reply("Please, enter message only number type")