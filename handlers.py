from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram import ParseMode
from api.courses_api import get_courses
from api.weather_api import get_weather

from api import get_vacancies

router=Router()

@router.message(F.text == "Кнопка 1")
async def process_btn_1(message: Message):
    await message_answer(text="Вы нажали кнопку №1")

@router.message(F.text == "Кнопка 2")
async def process_btn_2(message: Message):
    await message_answer(text="Вы нажали кнопку №2")

@router.message(Command(command=["keyboard"]))
async def process_keyboard_command(message: Message):
    await message.answer("Привет. Сделай выбор", reply_markup=simple_keyboard())

@router.message(Command(command=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет. Спроси у меня что-нибудь")

@router.message(Command(command=["help"]))
async def process_help_command(message: Message):
    await message.answer("Привет. Выбери нужное действие")

@router.message(Command(command=["weather"]))
async def process_weather_command(message: Message):
    await message.answer("Погода на сегодня:")

@router.message(Command(command=["vacancies"]))
async def process_vacancies_command(message: Message):
    data = get_vacancies()
    print(data)
    await message.answer("3 случайных вакансии python разработчика")
    for item in data:
        text = f"{item("name")}\nДата публикации; {item("created_at")}"
        await message.answer(text)

@router.message(Command(command=["courses"]))
async def process_courses_command(message: Message):
    await message.answer("Курс доллара и евро на сегодня")