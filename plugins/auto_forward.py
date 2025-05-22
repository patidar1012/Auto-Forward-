import asyncio, re
from pyrogram import Client, filters
from vars import ADMINS, FROM_DB, TARGET_DB

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(FROM_DB) & media_filter)
async def auto_forward(bot, message):
    file_caption = re.sub(r"@\w+|(_|\- |\.|\+|\[|\]\ )", " ", str(message.caption))
    await message.copy(
            chat_id=int(TARGET_DB),
            caption=file_caption
        )
    logger.info("Forwarded", message.caption, "from", FROM_DB, "to", TARGET_DB)
    await asyncio.sleep(1)