from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import dp, bot
import logging

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello bitch{message.from_user.full_name}")

@dp.message_handler(commands=["mem"])
async def start_mem(message: types.Message):
    photo = open("media/7d4f644e3015ea4aced4f1c7ed14be87.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "2 + 2"
    answers = [
        '2',
        "22",
        "4",
        "5",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="2 + 2 = 4",
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz2(call: types.CallbackQuery):
    question = "4 + 5"
    answers = [
        '9',
        '8',
        '5',
        '45'

    ]


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="4 + 5 = 9"


    )
@dp.message_handler()
async def echo (message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        message.text **= 2
        await bot.send_message(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
