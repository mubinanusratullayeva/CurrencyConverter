from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram import Router

cmd_router = Router()

@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    txt = ("""Hello, 
            welcome to ExchangeRate Bot!
            for help send /help command to us""")
    await message.answer(text=txt)
