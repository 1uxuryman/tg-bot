from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        message.text **= 2
        await bot.send_message(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
