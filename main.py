from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

bot = Client(
    "my first projrct",
    api_id=15801427,
    api_hash="b313f70d21884aa514b86ba1d1057da9",
    bot_token="5256333435:AAE6eZQLtVfLe32EOMXy9YcwDPo5GCQUTqM",
    plugins = {"root": "bot" },
    sleep_threshold=5
)

 


bot.run()
