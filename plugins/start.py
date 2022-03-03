from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 
from Script import script

#
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
#        buttons = [[
#            InlineKeyboardButton('🧗 Updates', url=f'https://t.me/TamilBots'),
#            InlineKeyboardButton('👨‍💻 Support chat, url=f'https://t.me/TamilSupport')
#        ]]
        buttons = [
            [
                InlineKeyboardButton('🤖 Updates', url='https://t.me/TamilBots')
            ],
            [
                InlineKeyboardButton('🤖 Updates', url='https://t.me/TamilBots'),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=https://telegra.ph/file/7e56d907542396289fee4.jpg,
            caption=script.START_TXT.format(message.from_user.first_name),
            reply_markup=reply_markup,
            parse_mode='html'
        )

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- '{filename}'\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
