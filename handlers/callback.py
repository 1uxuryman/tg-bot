from aiogram import types, Dispatcher
from config import bot


# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
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


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button_call_1")
