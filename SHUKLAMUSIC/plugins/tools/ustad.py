from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from SHUKLAMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/GREATPERSON_XD")
                ],
                [InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/LEGEND_TOSU")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/GREATPERSON_xd")
                ],
                [InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/LEGEND_TOSU")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/Greatperson_xd")
                ],
                [InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/Legend_Tosu")
            ]
            ]
        ),
    )
