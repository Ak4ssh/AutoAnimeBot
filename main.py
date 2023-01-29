import asyncio
import os
import requests
import telethon
import time
from random import randint 
import shutil
import psutil
import os
import asyncio
import sys
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
import sys
import dotenv
dotenv.load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUDO = list(map(int, os.getenv("SUDO").split()))
rem = randint(1, 10)
re = randint(1, 99)
class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


text = """---------------------------------
    ╔════╗
    ╚═╗╔═╝
    ╔═╣╠═╗
    ║╔╣╠╗║
    ║╚╣╠╝║
    ╚═╣╠═╝
    ╔═╝╚═╗ 
    ╚════╝ 
---------------------------------
"""
client = telethon.TelegramClient(None, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

async def main():
    for x in SUDO:
        try:
            await client.send_message(x,"Bot Has been restarted")
        except:pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())  

@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):

    but = [
        [
            telethon.Button.inline("Sites", b"Acc"),
            telethon.Button.inline("Jet", b"Proxys"),
            telethon.Button.inline("Casino", b"Proxys"),
        ],
        [
            telethon.Button.url("Support", url=("https://t.me/Aviatorhacksucessfully")),
            telethon.Button.url("Owner", url=("https://t.me/TheVenomXD")),
        ]
    ]
    await e.reply(f"**Welcome Sir!\n\nI'm Predictor Aviator Bot \nMade for Predicting Signal From Different Sites\n\nMade with ❤️ By @TheVenomXD**\n\n**You can add your funds manually by command /buy no third party.", buttons=but)

@client.on(telethon.events.CallbackQuery)
async def _(e):
    if e.data == b"Admin":
        if e.query.user_id not in SUDO:
            await e.client.send_message(e.chat.id, "You have no access to bot\n\n Get It From @TheVenomXD")
            return
        but = [
            [
                telethon.Button.inline("📊 Staus", b"Stat"),
            ],
            [
                telethon.Button.inline("🔄 Restart", b"Restart"),
                telethon.Button.inline("Back", b"Home")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Predictor Aviator Bot \nMade for Predicting Signal From Different Sites\n\nMade with ❤️ By @TheVenomXD**\n\n**You can add your funds manually by command /buy no third party.", buttons=but)
    elif e.data == b"Acc":
        if e.query.user_id not in SUDO:
            await e.client.send_message(e.chat.id, "You have no access to bot\n\n Get It From @TheVenomXD")
            return
        but = [
            [
                telethon.Button.inline("1 Win", "voot"),
                telethon.Button.inline("1xBet", "zee5"),
                telethon.Button.inline("Hollywood Bet", "alt"),
            ],
            [
                telethon.Button.inline("Pinup", "hoichoi"),
                telethon.Button.inline("MostBet", "Proxys"),
                telethon.Button.inline("Premier Bet", "Proxys"),
            ],
            [
                telethon.Button.inline("Back", b"Home")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Predictor Aviator Bot \nMade for Predicting Signal From Different Sites\n\nMade with ❤️ By @TheVenomXD**\n\n**You can add your funds manually by command /buy no third party.", buttons=but)
    elif e.data == b"Home":
        but = [
        [
            telethon.Button.inline("Sites", b"Acc"),
            telethon.Button.inline("Jet", b"Proxys"),
            telethon.Button.inline("Casino", b"Proxys"),
        ],
        [
            telethon.Button.url("Support", url=("https://t.me/Aviatorhacksucessfully")),
            telethon.Button.url("Owner", url=("https://t.me/TheVenomXD")),
        ]
    ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Predictor Aviator Bot \nMade for Predicting Signal From Different Sites\n\nMade with ❤️ By @TheVenomXD**\n\n**You can add your funds manually by command /buy no third party.", buttons=but)
    elif e.data == b"Stat":
        start = time.time()
        await e.answer('\nWait Checking Stats', alert=True)
        end = round((time.time() - start) * 1000)

        def humanbytes(size):

            if size in [None, ""]:
                return "0 B"
            for unit in ["B", "KB", "MB", "GB"]:
                if size < 1024:
                    break
                size /= 1024
            return f"{size:.2f} {unit}"

        def time_formatter():
            if tmp != "":
                if tmp.endswith(":"):
                    return tmp[:-1]
                else:
                    return tmp
            else:
                return "0 s"
        total, used, free = shutil.disk_usage(".")
        cpuUsage = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        upload = humanbytes(psutil.net_io_counters().bytes_sent)
        down = humanbytes(psutil.net_io_counters().bytes_recv)
        TOTAL = humanbytes(total)
        USED = humanbytes(used)
        FREE = humanbytes(free)
        tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
        await e.client.send_message(e.chat.id, tex, buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])
    elif e.data == b"Restart":
        await e.answer('\nRestarting Bot Wait', alert=True)
        os.execl(sys.executable, sys.executable, "-m", "main")
    elif e.data == b"Proxys":
        await e.answer('Comming Soon', alert=True)
    else:
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message(f"Signal Is: `{rem}.{re}`")



RIZ_PIC = "https://telegra.ph/file/6166c9ac5b281a3039afa.jpg"

rizoel = f"✯ Predictor Aviator Bot ☆\n\n"
rizoel += f"═══════════════════\n"
rizoel += f"• 1 Month = ₹1500\n"
rizoel += f"• 2 Months + Private Server = ₹2300\n"
rizoel += f"• 5 Months Accurate Signals = ₹3700\n\n"
rizoel += f"**• Pay Using Above Bar code And send transaction Id Or Screenshot For Funds Will Be added In 5 seconds**\n\n"
rizoel += f"═══════════════════\n\n"   

                                  
@client.on(telethon.events.NewMessage(incoming=True, pattern='/buy', func=lambda e: e.is_private))
async def alive(event):
    await event.client.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Aviatorhacksucessfully"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TheVenomXD")
        ]
        ]
        )

@client.on(telethon.events.InlineQuery)
async def inline_alive(o):
    if o.original_update.user_id in acc:
        return
    """
    ishan=[
        await o.builder.article(
                text="• **Induced Promotion Bot \nSubscribtion Cost: 200Rs per Month •**",
                buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]],
                title="Induced Promotion Bot",
                description="Use Our To Promote your self For Selling\nAuto Post Sender In Multiple groups",
                thumb=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
                content=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
        )
    ]
    """
    ishan = [
        await o.builder.photo(
            "https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg",
            text="Induced Checker Bot \n\nAll main Checking Features Given Below\n👇\n\nAccs: \n\n• Zee5 Bulk Accs Checker\n• Alt Balaji Bulk Accs Checker\n• Voot Bulk Accs Checker\n\nComing Soon 🔥 :\n• Proxy Checker \n• Cc Bulk Checker\n#NOTE: It's Free & Public For Other Users \n\nDemoBot: @InducedChecker_Bot\n\n© @InducedBots || @Teaminduced",
            buttons=[
                [
                    telethon.Button.url("• Support •", url="t.me/InducedBotsSupport"),
                    telethon.Button.url("• Repo •", url="https://github.com/IshanSingla/InducedCheckerBot")
                ],
                [
                    telethon.Button.url("• Deploy to Heroku •", url="https://heroku.com/deploy?template=https://github.com/IshanSingla/InducedCheckerBot"),
                    telethon.Button.url("• Tutorial •", url="https://github.com/IshanSingla/InducedCheckerBot")
                ]
            ],
            link_preview=False,
        )
    ]
    await o.answer(
        ishan,
        cache_time=300,
        switch_pm="👥 Induced Promotion Bot",
        switch_pm_param="start",
    )
    
print(text)
try:
    client.run_until_disconnected()
except:
    os.execl(sys.executable, sys.executable, "-m", "main")
