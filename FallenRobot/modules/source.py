from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/90552395a5e96d0e7fab9.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝖠𝗅𝗂𝖺-🇯🇴](t.me/Aliaqueen_bot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝖱𝗈𝗀𝗎𝖾](t.me/Oriksonic)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**𝖺𝗅𝗂𝖺 𝗂𝗌 𝖺 𝗉𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝖺𝗇𝖺𝗀𝖾𝗋 𝖻𝗈𝗍 ᴜ ᴄᴀɴ ᴜsᴇ 𝖠𝖫𝖨𝖠 ʙᴏᴛ ғᴏʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/Oriksonic"
                    ),
                    InlineKeyboardButton(
                        "•𝗌𝗎𝗉𝗉𝗈𝗋𝗍•",
                        url="https://t.me/botsupportastra"
                    ),
                ],
                [
                    InlineKeyboardButton("• ➕ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ➕ •", url="https://t.me/ZenXrobot?startgroup=true"),     
                ],
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"

