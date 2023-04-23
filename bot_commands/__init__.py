import logging as lgg
from aiogram import Bot, Dispatcher, types, executor
import requests, json, random, os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ.get("TLG_BOT_TOKEN"))
dp = Dispatcher(bot)