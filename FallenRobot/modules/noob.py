
import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from FallenRobot import pbot as bot

Alia = "https://telegra.ph/file/fc41fe013de74a1648669.jpg"


@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Alia,
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝖠𝗅𝗂𝖺](t.me/Aliaqueen_bot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/pythonxgamer"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
