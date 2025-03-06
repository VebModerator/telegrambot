from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router=Router()

@router.message(Command(command=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет. Спроси у меня что-нибудь")

@router.message(Command(command=["help"]))
async def process_start_command(message: Message):
    await message.answer("Привет. Выбери нужное действие")

@router.message(Command(command=["weather"]))
async def process_start_command(message: Message):
    await message.answer("Погода на сегодня:")

@router.message(Command(command=["vacancies"]))
async def process_start_command(message: Message):
    await message.answer("3 случайных вакансии python разработчика")

@router.message(Command(command=["сщгкыуы"]))
async def process_start_command(message: Message):
    await message.answer("Курс доллара и евро на сегодня")