import os
import logging
import asyncio
from decouple import config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from random import choice 
from pyrogram import Client, filters

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

anibot = Client(
    'AutoAnime',
    api_id=Var.APP_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
)

anibot.start()

if Var.STRING:
    bot = Client('bot', api_id=Var.APP_ID, api_hash=Var.API_HASH, session_string=Var.STRING)
else:
    bot = None

bot.start()

piclist = [
    "https://te.legra.ph/file/bbf0b40a031dc3987ca36.jpg",
    "https://te.legra.ph/file/d8f4efcbfd88612ebdc70.jpg",
    "https://te.legra.ph/file/b253b1e6b4e2e9fecce50.jpg",
    "https://te.legra.ph/file/30dddb618bb44a322e559.jpg",
    "https://te.legra.ph/file/41fff04624f04e5599a3a.jpg",
]
    
Array = choice(piclist)
bisi = "/"

@anibot.on_message(filters.private & filters.incoming & filters.command(['/start']))
async def _start(_, ok: Message):
        animu = f"**Hi {ok.user.first_name}!\n\nI Am An Auto Anime Bot Uploads Latest Anime That Are Being Alerted On __animepahe.com__\n\nCurrently Uploading & Alerting About New Animes On @{TO_CHANNEL}\n\nMade With ❤**"
        await ok.reply_photo(
        photo=Array,
        caption=animu,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/KyuKaizenX")
                ],]
            ))


@bot.on_message(filters.NewMessage(incoming=True, chats=Var.FROM_CHANNEL))
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await bot.send_file(Var.TO_CHANNEL, photo, caption = event.text, link_preview = False)
            elif event.media:
                try:
                    if event.media.webpage:
                        await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False)
                        return
                except:
                    media = event.media.document
                    await bot.send_file(Var.TO_CHANNEL, media, caption = event.text, link_preview = False)
                    return
            else:
                await bot.send_message(Var.TO_CHANNEL, event.text, link_preview = False)
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
