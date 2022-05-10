from AttachMents.starter import start
from AttachMents.anime import Anime
from AttachMents.manga import Manga
from AttachMents.nhentai import Nhentai
from config import bot

try:
    start()
    Anime()
    Manga()
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()