from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 
from Script import script
from pyrogram.emoji import *


@Client.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(c, m, cb=False):
    button = [[
        InlineKeyboardButton(f'{MONEY_BAG} dev', url='https://t.me/tamilbots')
        ],[
        InlineKeyboardButton(f'{HOUSE_WITH_GARDEN} Home', callback_data='back'),
        InlineKeyboardButton(f'{NO_ENTRY} 𝙲𝚕𝚘𝚜𝚎', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await m.message.edit(
            text=script.HELP_USER.format(m.from_user.first_name),
            reply_markup=reply_markup,
            disable_web_page_preview=True,
        )
    else:
        await m.reply_photo(
            photo="https://telegra.ph/file/7e56d907542396289fee4.jpg",
            caption=script.HELP_USER.format(m.from_user.first_name),
            reply_markup=reply_markup,
            parse_mode='html'
          
        )


################## start commamd ##################

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(c, m, cb=False):

    button = [[
        InlineKeyboardButton(f'{MAN_TEACHER_LIGHT_SKIN_TONE} TamilBots', url=f'https://t.me/tamilbots'),
        InlineKeyboardButton(f'{ROBOT} About', callback_data='about')
        ],[
        InlineKeyboardButton(f'{INFORMATION} Help', callback_data="help"),
        InlineKeyboardButton(f'{NO_ENTRY} Close', callback_data="close")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await m.message.edit(
            text=script.START_TEXT.format(user_mention=m.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await m.reply_photo(
            photo="https://telegra.ph/file/7e56d907542396289fee4.jpg",
            caption=script.START_TEXT.format(user_mention=m.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'

        ) 


################## about command ##################

@Client.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(c, m, cb=False):
    me = await c.get_me()

    button = [[
        InlineKeyboardButton(f'{HOUSE_WITH_GARDEN} Home', callback_data='back'),
        InlineKeyboardButton(f'{MONEY_BAG} dev', url='https://t.me/tamilbots')
        ],[
        InlineKeyboardButton(f'{NO_ENTRY} Close', callback_data="close")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await m.message.edit(
            text=script.ABOUT.format(bot_name=me.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await m.reply_text(
            text=script.ABOUT.format(bot_name=me.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
        )


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
