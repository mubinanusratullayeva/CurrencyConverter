from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router

from config import response_uzs, response_usd, response_rub, response_eur

cmd_router = Router()


@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    txt = ("""Hello, 
            welcome to ExchangeRate Bot!
            for help send /help command to us""")
    await message.answer(text=txt)


@cmd_router.message(Command('help'))
async def cmd_help(message: Message):
    txt = """
        /courses - know exchange rates
        /dollar - know the dollar exchange rate
        /euro - know the euro exchange rate
        /rouble - know the rouble exchange rate
        
        Send an amount and the bot will return it to you in different currencies"""
    await message.answer(text=txt)


@cmd_router.message(Command('courses'))
async def cmd_courses(message: Message):
    data_usd = response_uzs.json()['conversion_rates']
    data_eur = response_eur.json()['conversion_rates']
    data_rub = response_rub.json()['conversion_rates']

    txt = "Today's exchange rates:\n"
    txt += f"1 Dollar - {data_usd['UZS']} sum\n"
    txt += f"1 EUR - {data_eur['UZS']} sum\n"
    txt += f"1 Rouble - {data_rub['UZS']} sum\n"

    await message.answer(text=txt)


@cmd_router.message(Command('dollar'))
async def cmd_dollar(message: Message):
    data = response_usd.json()

    txt = ''
    for course in data['conversion_rates']:
        if course == 'UZS':
            txt = f"1 Dollar = {data['conversion_rates'][course]} sum"

    await message.reply(txt)


@cmd_router.message(Command('euro'))
async def cmd_euro(message: Message):
    data = response_eur.json()

    txt = ''
    for course in data['conversion_rates']:
        if course == 'UZS':
            txt = f"1 Euro = {data['conversion_rates'][course]} sum"

    await message.reply(txt)


@cmd_router.message(Command('rouble'))
async def cmd_rouble(message: Message):
    data = response_rub.json()

    txt = ''
    for course in data['conversion_rates']:
        if course == 'UZS':
            txt = f"1 Rouble = {data['conversion_rates'][course]} sum"

    await message.reply(txt)
