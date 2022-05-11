
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

try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    session = config("STRING")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)

    if STRING: 
        session_name = str(STRING)
        print("String 1 Found")
        datgbot = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await datgbot.start()
            botme = await datgbot.get_me()
            botid = telethon.utils.get_peer_id(botme)
            CLIENTS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        pass
        session_name = "AutoAnimeBot"
        datgbot = TelegramClient(session_name, APP_ID, API_HASH)
        try:
            await datgbot.start()
        except Exception as e:
            print(str(e))
except Exception as e:
    print(str(e))


@datgbot.on(events.NewMessage(incoming=True, chats=frm))
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await datgbot.send_file(tochnl, photo, caption = event.text, link_preview = False)
            elif event.media:
                try:
                    if event.media.webpage:
                        await datgbot.send_message(tochnl, event.text, link_preview = False)
                        return
                except:
                    media = event.media.document
                    await datgbot.send_file(tochnl, media, caption = event.text, link_preview = False)
                    return
            else:
                await datgbot.send_message(tochnl, event.text, link_preview = False)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot Initialized Perhaps Started!")
datgbot.run_until_disconnected()
