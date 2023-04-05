from aiogram import Bot, Dispatcher
from config import load_config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = load_config('../chatGPT_bot/.env')
BOT_TOKEN = config.tg_bot.BOT_TOKEN
OPENAI_TOKEN = config.tg_bot.OPENAI_TOKEN
USERS = config.tg_bot.USERS
ADMIN = config.tg_bot.ADMIN

storage = MemoryStorage()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
