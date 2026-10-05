import asyncio
import os
from aiohttp import web
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError

API_ID = 30687248
API_HASH = "7dba2dedb27be41e1bf04c583f96eaf9"

SESSION_STRING = "1ApWapzMBu57a3VtJCTb6DEV2jk1o_TRXPFCgNeuMePfbDZR8vKoCSBrIsm4xRoLKtRqStLNzbUfJ-Kg0B_kKxnletN3_SQUXVNQiHfy8YDKQMkjjPvEOT9_vjKtptxlnzfjwH_zmFyEJp0qehtTUq3vfdLdZJ421TjGp7iXiG-miKIVduuhu0y1GFF5BZxhNeiHTp-pxQqQm9yYdAw s_4Zj0l1CzZFPiohVPhV-QUkp1un1CZH5osCsaBv0jD2IV4dcS6h7QoeYi2VdTyGKcGeRwIZJItCuagSXcXbw0oRaIq0niz66jsvxQz340jofNnZyzrIN6HkJdrOM8NX2LR1m3xVujs6A="

GROUPS = [
    "turk_forum",
    "instagram_akaunt_savdo_chati",
    "forum_uzb_rubl",
    "Gifts_Savdosi",
    "https://t.me/+RXaYowysCqRlNWIy",
    "uzforum_guruh"
]

MESSAGE_TEXT = """⚠️ **Dasturchilar bu botni yopilishini xohlayapti...**

Chunki odamlar dasturchilarga millionlab so‘m bermasdan, **1 daqiqada** o‘z botini ochib olyapti!

Sen ham o‘z shaxsiy botingni yarat:
🎬 **Kino bot** (kodli kino kanallar uchun)  
📥 **Yuklovchi bot** (Instagram, TikTok, YouTube)  
⭐️ **Stars / Premium sotish boti**  
📱 **Virtual nomerlar boti**

🎁 **Hozir kirganlarga dastlabki kunlar MUTLAQO BEPUL!**

Hech qanday to‘lovsiz, shunchaki kir va botingni ol 👇  
👉 @abubakrbuilderbot"""

DELAY_BETWEEN = 15
INTERVAL_AFTER_ALL = 60

clean_session = SESSION_STRING.replace(" ", "").strip()
client = TelegramClient(StringSession(clean_session), API_ID, API_HASH)

async def sender_task():
    await client.start()
    print("Userbot muvaffaqiyatli ishga tushdi!")

    while True:
        for group in GROUPS:
            try:
                if "+" in group or "joinchat" in group:
                    entity = await client.get_entity(group)
                else:
                    entity = group

                await client.send_message(entity, MESSAGE_TEXT)
                print(f"Yuborildi: {group}")
            except FloodWaitError as e:
                print(f"Telegram cheklovi: {e.seconds} soniya kutilmoqda...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Yuborilmadi ({group}): {e}")

            await asyncio.sleep(DELAY_BETWEEN)

        print(f"Barcha guruhlarga yuborildi. {INTERVAL_AFTER_ALL} soniya kutilmoqda...")
        await asyncio.sleep(INTERVAL_AFTER_ALL)

# Render bepul rejimda o'chib qolmasligi uchun mini web-server
async def handle(request):
    return web.Response(text="Userbot faol ishlamoqda!")

async def main():
    asyncio.create_task(sender_task())
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server {port}-portda ishga tushdi")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
