
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
    datgbot = TelegramClient(StringSession(STRING), APP_ID, API_HASH)
    
    if STRING: 
        session_name = str(STRING)
        print("String 1 Found")
        Akash = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Akash.start()
            await Akash(functions.account.UpdateProfileRequest(last_name="• 1 •"))
            await Akash(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            botme = await Akash.get_me()
            botid = telethon.utils.get_peer_id(botme)
            CLIENTS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        pass
        session_name = "rizoelxspam"
        Akash = TelegramClient(session_name, APP_ID, API_HASH)
        try:
            await Akash.start()
        except Exception as e:
            pass

    

@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi `{ok.user.first_name}`!\n\nI am a channel auto-post bot!! Read /help to know more!\n\nI can be used in only two channels (one user) at a time. Kindly deploy your own bot.")


@datgbot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("Set All Vars And Bot Started Nothing More ;)")

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
