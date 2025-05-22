import asyncio
from pyrogram import Client, filters
from vars import ADMINS, FROM_DB, TARGET_DB

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(FROM_DB) & media_filter)
async def auto_forward(bot, message):
    await message.copy(
        chat_id=int(TARGET_DB)
    )