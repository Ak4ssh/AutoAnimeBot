import os
import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sessions import StringSession
from telethon import Button

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
    FEED_URL= os.environ.get("FEED_URL", None)

anibot = TelegramClient('anibot', Var.APP_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

anibot.start()

if Var.STRING:
    session_name = str(Var.STRING)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

bot.start()

btn = [
      [ 
      Button.url("• Watch •", "https://t.me/TheVenomXD"),
      Button.url("• Comments •", "https://t.me/DNHxHELL")
      ],
      [
      Button.url("• Support •", "t.me/TheVenomXD")
      ],
      [
      Button.inline("• Chat Group •", "t.me/TheVenomXD")
      ],
      ]


@anibot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await anibot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi {ok.user.first_name}!\n\nPlease use /help to get started.\n\nNote: I can only give you the files of anime that are currently bring airied at @AutoAnimeUploads.")

@bot.on(events.NewMessage(incoming=True, chats=Var.FROM_CHANNEL))
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await bot.send_file(Var.TO_CHANNEL, photo, caption = event.text, link_preview = False, buttons=btn)
            elif event.media:
                try:
                    if event.media.webpage:
                        await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False, buttons=btn)
                        return
                except:
                    media = event.media.document
                    await bot.send_file(Var.TO_CHANNEL, media, caption = event.text, link_preview = False, buttons=btn)
                    return
            else:
                await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False, buttons=btn)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


def send_msg(title,msg):
    print("Detected a new release!")
    headers={'Connection':'close'}
    requests.Session().post(f'https://api.telegram.org/bot'+Var.BOT_TOKEN+'/sendMessage?chat_id='+Var.TO_CHANNEL+'&text='+title+'%0A'+msg, headers=headers)
    
def main():
    prev=None #a shit scheme to save previous title to stop repitition
    #print("running..."+str(i), end='\r')
    news=feedparser.parse(Var.FEED_URL)
    for entry in news.entries:
        parsed_date = parser.parse(entry.published).replace(tzinfo=None)
        #parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None)
        now_date = datetime.utcnow()

        published_2_minutes_ago = now_date - parsed_date < timedelta(minutes=2)
        #print(published_5_minutes_ago)
        if published_2_minutes_ago and entry.title!=prev:
            if prev==None:
                prev=entry.title
            send_msg(entry.title,entry.links[0].href)
            print(entry.links[0].href)    

print("Bot Initialized Perhaps Started!")
bot.run_until_disconnected()
