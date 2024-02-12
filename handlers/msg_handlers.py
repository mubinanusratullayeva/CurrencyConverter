import requests
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router

from config import courses

msg_router = Router()


@msg_router.message()
async def convert_dollar(message: Message):
    try:
        foo = int(message.text)
        s = f"{foo} sum: \n"
        s += f"{foo * courses['UZB']: .2f} sum"
        s += f"{foo * courses['EUR']: .2f} euro"
        s += f"{foo * courses['RUB']: .2f} ruble"
        await message.answer(text=s)
    except
