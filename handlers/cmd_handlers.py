from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router

from config import courses, response

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
    txt = "Today's exchange rates:\n"
    for course in response.json():
        if course['Ccy'] in ['USD', 'EUR', 'RUB']:
            courses[course['Ccy']] = float(course['Rate'])
            txt += f"1 {course['CcyNm_EN']} - {course['Rate']} sum\n"
    await message.answer(text=txt)


@cmd_router.message(Command('dollar'))
async def cmd_dollar(message: Message):
    txt = ''
    for course in response.json():
        if course['Ccy'] in 'USD':
            txt = f"1 {course['CcyNm_EN']} = {course['Rate']} sum"
    await message.reply(txt)


@cmd_router.message(Command('euro'))
async def cmd_dollar(message: Message):
    txt = ''
    for course in response.json():
        if course['Ccy'] in 'EUR':
            txt = f"1 {course['CcyNm_EN']} = {course['Rate']} sum"
    await message.reply(txt)


@cmd_router.message(Command('rouble'))
async def cmd_dollar(message: Message):
    txt = ''
    for course in response.json():
        if course['Ccy'] in 'RUB':
            txt = f"1 {course['CcyNm_EN']} = {course['Rate']} sum"
    await message.reply(txt)