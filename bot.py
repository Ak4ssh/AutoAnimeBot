import os
import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
print("Initializing RyzenApi")
print("Initializing Repo")

class Var(object):
    STRING = os.environ.get("STRING", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    TO_CHANNEL = os.environ.get("TO_CHANNEL", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

anibot = TelegramClient('anibot', Var.APP_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

anibot.start()

if Var.STRING:
    session_name = str(Var.STRING)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

bot.start()


@anibot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await anibot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi ||{ok.user.first_name}||!\n\nI am an Auto Anime bot!!\n\nRead /help to know more about me\n\nA part of @ArrayCore\n\n Made With ❤ By @TheVenomXD")

@bot.on(events.NewMessage(incoming=True, chats=Var.FROM_CHANNEL))
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await bot.send_file(Var.TO_CHANNEL, photo, caption = event.text, link_preview = False, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("•ᴡᴀᴛᴄʜ•", url=f"https://t.me/TheVenomXD")]]))
            elif event.media:
                try:
                    if event.media.webpage:
                        await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("•ᴡᴀᴛᴄʜ•", url=f"https://t.me/TheVenomXD")]]))
                        return
                except:
                    media = event.media.document
                    await bot.send_file(Var.TO_CHANNEL, media, caption = event.text, link_preview = False, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("•ᴡᴀᴛᴄʜ•", url=f"https://t.me/TheVenomXD")]]))
                    return
            else:
                await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("•ᴡᴀᴛᴄʜ•", url=f"https://t.me/TheVenomXD")]]))
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot Initialized Perhaps Started!")
bot.run_until_disconnected()
