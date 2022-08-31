from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello bitch {message.from_user.full_name}")


# @dp.message_handler(commands=["mem"])
async def start_mem(message: types.Message):
    photo = open("media/7d4f644e3015ea4aced4f1c7ed14be87.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
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


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(start_mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
