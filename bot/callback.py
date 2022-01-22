from pyrogram import Client as bot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

@bot.on_callback_query()
async def cb_handler(bot, query):

    if query.data == "close":
        await query.message.delete()

    elif query.data == "start":
        button = [[     
          InlineKeyboardButton("⚠️ 𝖧𝖾𝗅𝗉", callback_data="help"),
          InlineKeyboardButton("🛡️ 𝖠𝖻𝗈𝗎𝗍", callback_data="about")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.START_TXT, reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "help":
       button = [[
          InlineKeyboardButton("🦵 Kick", callback_data="kick"),
          InlineKeyboardButton("👋 Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("🤫 Mute", callback_data="mute"),
          InlineKeyboardButton("😌 Unmute", callback_data="unmute"),
          InlineKeyboardButton("🎗️ User Info", callback_data="usrinfo")
          ],[
          InlineKeyboardButton("🛡️ About", callback_data="about"),
          InlineKeyboardButton("🗼 Home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close"),
          InlineKeyboardButton("⬅️ Back", callback_data="start")
          ]]
   
       await query.message.edit_text(Jk.HELP_TXT,reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "about":
       button = [[
          InlineKeyboardButton("⚠️ help", callback_data="help"),
          InlineKeyboardButton("🗼 Home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close"),
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]]
       await query.message.edit_text(Jk.ABOUT_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "home":
       button = [[
          InlineKeyboardButton("⚠️ Help", callback_data="help"),
          InlineKeyboardButton("🛡️ About", callback_data="about")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
       await query.message.edit_text(Jk.START_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "kick":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.KICK_TXT,reply_markup=InlineKeyboardMarkup(button))
     
    elif query.data == "ban":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.BAN_TXT,reply_markup=InlineKeyboardMarkup(button)) 
    elif query.data == "mute":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.MUTE_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "unmute":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.UNMUTE_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "usrinfo":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.USERINFO_TXT,reply_markup=InlineKeyboardMarkup(button))

