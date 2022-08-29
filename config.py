from aiogram import Bot, Dispatcher
from decouple import config as token

TOKEN = token("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



