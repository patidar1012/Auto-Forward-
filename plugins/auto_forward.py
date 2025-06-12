import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_DB, TO_DB

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

media_filter = filters.document | filters.video
lock = asyncio.Lock()
forwarded = 0

@Client.on_message(filters.chat(FROM_DB) & media_filter)
async def auto_forward(bot, message):
    global forwarded
    file_caption = re.sub(r"(𝗧𝗛𝗘 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 )|(𝙿𝚘𝚠𝚎𝚛e𝚍 𝙱𝚢 ➥  @Theprofessers)|(❤️‍🔥 Join ~ [ @Moonknight_media ])|(\n🔸 Upload By \[@BlackDeath_0\])|(\n❤️‍🔥 Join ~ \[@Moonknight_media\])|(@Ac_Linkzz)|(\n⚡️Join:- \[@BlackDeath_0\]‌‌)|(EonMovies)|(\nJOIN 💎 : @M2LINKS)|@\w+|(_|\- |\.|\+)", " ", str(message.caption))
    file_caption = f"""{file_caption}\n➖➖➖➖➖➖➖➖➖➖
 <b>Powered By:</b> <a href='https://t.me/MovieTimesTV'><b>Mᴏᴠɪᴇ Tɪᴍᴇs™</b></a>
➖➖➖➖➖➖➖➖➖➖"""
    async with lock:
        try:
            await message.copy(
                    chat_id=int(TO_DB),
                    caption=file_caption
                )
            forwarded += 1
            logger.info(f"Forwarded {message.caption} from {FROM_DB} to {TO_DB}\nforwarded {forwarded} files")
            await asyncio.sleep(1)
            if forwarded % 20 == 0:
                logger.info("⏸️ 20 files sent! Taking a break of 30 seconds...")
                await asyncio.sleep(30)
        except FloodWait as e:
            logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
            await asyncio.sleep(e.value + 2)
            await message.copy(
                    chat_id=int(TO_DB),
                    caption=file_caption
                )
            forwarded += 1
            logger.info(f"Forwarded {message.caption} from {FROM_DB} to {TO_DB}\nforwarded {forwarded} files")
            await asyncio.sleep(1)
            if forwarded % 20 == 0:
                logger.info("⏸️ 20 files sent! Taking a break of 30 seconds...")
                await asyncio.sleep(30)
