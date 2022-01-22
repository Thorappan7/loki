from pyrogram import Client as bot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    button1 = [[
    InlineKeyboardButton("⚠️ Help", callback_data="help"),
    InlineKeyboardButton("🛡️ About", callback_data="about"),
    ],[
    InlineKeyboardButton("🚮 Close", callback_data="close")
    ]]
    text = Jk.START_TXT
    reply_markup = InlineKeyboardMarkup(button1)
    bot.send_photo(message.chat.id, Jk.PICS,
    caption=text,
    reply_markup=reply_markup,
    
    )
        
    
@bot.on_message(filters.command("help"))
def help(bot, message):
    button2 = [[
          InlineKeyboardButton("🦵 Kick", callback_data="kick"),
          InlineKeyboardButton("👋 Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("🤫 Mute", callback_data="mute"),
          InlineKeyboardButton("😌 Unmute", callback_data="unmute"),
          InlineKeyboardButton("🎗️ User Info", callback_data="usrinfo")
          ],[
          InlineKeyboardButton("🛡️ about", callback_data="about"),
          InlineKeyboardButton("🗼 home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close"),
          InlineKeyboardButton("⬅️Back", callback_data="start")
          ]]
    reply_markup = InlineKeyboardMarkup(button2)
    bot.send_photo(message.chat.id, Jk.PICS,
    caption=Jk.START_TXT,
    reply_markup=reply_markup
    )
    

@bot.on_message(filters.command("photo"))
def photo(bot, message):
    bot.send_photo(message.chat.id, Jk.PICS,)

@bot.on_message(filters.command("alive"))
def alive(bot, message):
    buttonw = [[
    InlineKeyboardButton("⚠️ Help", callback_data="help"),
    InlineKeyboardButton("🛡️ About", callback_data="about")
    ],[
    InlineKeyboardButton("🗼 Home", callback_data="home")
    ],[
    InlineKeyboardButton("🚮 Close", callback_data="close")
    ]]

    bot.send_photo(message.chat.id, Jk.PICS,
    caption=Jk.START_TXT,
    reply_markup=InlineKeyboardMarkup(buttonw)
    )
