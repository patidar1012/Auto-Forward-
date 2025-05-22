import asyncio, re
from pyrogram import Client, filters
from vars import ADMINS, FROM_DB, TARGET_DB

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(FROM_DB) & media_filter)
async def auto_forward(bot, message):
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return
    file_caption = re.sub(r"(JOIN 💎 : @M2LINKS)|@\w+|(_|\- |\.|\+|\[|\]\ )", " ", str(message.caption))
    await message.copy(
            chat_id=int(TARGET_DB),
            caption=file_caption
        )
    logger.info(f"Forwarded {message.caption} from {FROM_DB} to {TARGET_DB}")
    await asyncio.sleep(1)