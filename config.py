import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
tsession = os.environ.get('TSESSION)

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
Client = TelegramClient('Client', api_id, api_hash).start(tsession=tsession)
