from pyrogram.types import ChatPermissions
from pyrogram import Client as bot , filters

@bot.on_message(filters.command("ban")&filters.group)
def ban(bot, message):
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} you are banned!!!")

@bot.on_message(filters.command("unban")&filters.group)
def unban(bot, message):
    bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} unbanned enjoy !!!")

@bot.on_message(filters.command("mute")&filters.group)
def mute(bot, message):
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} വിളച്ചിൽ എടുക്കരുത് കേട്ടോ .. കുറച്ച് നേരം മിണ്ടാതെ ഇരിക്ക് !!!")

@bot.on_message(filters.command("unmute")&filters.group)
def unmute(bot, message):
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(can_send_media_messages=True, can_send_messages=True, can_send_other_messages=True))
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} ഗോപാലകൃഷ്ണനോട് മൊതലാളി ഷമിച്ചിരിക്കുന്നു!!!")
