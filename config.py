from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("21209802")
APP_HASH = os.environ.get("eed1c8387c6ee80009527e07d9d58cc0")
BOT_USERNAME = os.environ.get("Gmail_huntingbot")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("6807629743:AAHsnFL_eb9F-egK2yjvvxVgKWIcQIhpNDA")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
