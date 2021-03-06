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
          InlineKeyboardButton("â ï¸ ð§ð¾ðð", callback_data="help"),
          InlineKeyboardButton("ð¡ï¸ ð ð»ððð", callback_data="about")
          ],[
          InlineKeyboardButton("ð® Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.START_TXT, reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "help":
       button = [[
          InlineKeyboardButton("ð¦µ Kick", callback_data="kick"),
          InlineKeyboardButton("ð Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("ð¤« Mute", callback_data="mute"),
          InlineKeyboardButton("ð Unmute", callback_data="unmute"),
          InlineKeyboardButton("ðï¸ User Info", callback_data="usrinfo")
          ],[
          InlineKeyboardButton("ð¡ï¸ About", callback_data="about"),
          InlineKeyboardButton("ð¼ Home", callback_data="home")
          ],[
          InlineKeyboardButton("ð® Close", callback_data="close"),
          InlineKeyboardButton("â¬ï¸ Back", callback_data="start")
          ]]
   
       await query.message.edit_text(Jk.HELP_TXT,reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "about":
       button = [[
          InlineKeyboardButton("â ï¸ help", callback_data="help"),
          InlineKeyboardButton("ð¼ Home", callback_data="home")
          ],[
          InlineKeyboardButton("ð® Close", callback_data="close"),
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]]
       await query.message.edit_text(Jk.ABOUT_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "home":
       button = [[
          InlineKeyboardButton("â ï¸ Help", callback_data="help"),
          InlineKeyboardButton("ð¡ï¸ About", callback_data="about")
          ],[
          InlineKeyboardButton("ð® Close", callback_data="close")
          ]]
       await query.message.edit_text(Jk.START_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "kick":
       button = [[
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.KICK_TXT,reply_markup=InlineKeyboardMarkup(button))
     
    elif query.data == "ban":
       button = [[
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.BAN_TXT,reply_markup=InlineKeyboardMarkup(button)) 
    elif query.data == "mute":
       button = [[
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.MUTE_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "unmute":
       button = [[
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.UNMUTE_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "usrinfo":
       button = [[
          InlineKeyboardButton("â¬ï¸Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.USERINFO_TXT,reply_markup=InlineKeyboardMarkup(button))

