import asyncio
from telethon import TelegramClient
from telethon.errors import FloodWaitError

API_ID = 30687248
API_HASH = "7dba2dedb27be41e1bf04c583f96eaf9"

# Guruhlar ro'yxati (private havola bilan birga)
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

# Guruhlar orasidagi kutish (soniya)
DELAY_BETWEEN = 15

# Davra tugagach keyingi aylanmagacha kutish (soniya)
INTERVAL_AFTER_ALL = 60

client = TelegramClient("user_session", API_ID, API_HASH)

async def main():
    await client.start()
    print("Userbot ishga tushdi!")

    while True:
        for group in GROUPS:
            try:
                # Private guruh havolasi bo'lsa entity qilib oladi
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

        print(f"Barcha guruhlarga yuborildi. {INTERVAL_AFTER_ALL} soniya kutilyapti...")
        await asyncio.sleep(INTERVAL_AFTER_ALL)

if __name__ == "__main__":
    client.loop.run_until_complete(main())
