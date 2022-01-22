from pyrogram import Client as bot, filters, emoji


MENTION = "[{}](tg://user?id={})"
text1="hi{} {} welcome to Group Chat"


group ="jangobotz"
@bot.on_message(filters.chat(group) &filters.new_chat_members)
async def welcome(bot, message):
    new_members = [u.mention for u in message.new_chat_members]

    TEXT2= text1.format(emoji.SPARKLES,",".join(new_members))
    await message.reply_text(TEXT2)

@bot.on_message(filters.command("leave") &filters.group)
def leave(bot, message):
    bot.send_message(message.chat.id, "നമ്മളില്ലേ...അല്ലേലും സ്വപ്നത്തിലെ കട്ടുറുമ്പ് ആവൻ ഞാനില്ല ..ഭൂമി ഉരുണ്ടതല്ലെ എവിടേലും വെച്ച് കാണാം")
    bot.leave_chat(message.chat.id )
