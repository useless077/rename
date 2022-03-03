from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 
from Script import script

@Clinton.on_message(filters.command(["start"]))
async def start(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Script.START_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='⭕ Cʜᴀɴɴᴇʟ ⭕', url=f'https://t.me/{Config.UPDATE_CHANNEL}'),
                                                 InlineKeyboardButton(text='⭕ Sᴜᴘᴘᴏʀᴛ ⭕', url=f'https://t.me/{Config.UPDATE_GROUP}') ],
                                               [ InlineKeyboardButton(text='👨‍💻 Dᴇᴘʟᴏʏ Nᴏᴡ', url='https://youtu.be/2FHgg8o1YY8'),                                                
                                                 InlineKeyboardButton(text='🔐 Cʟᴏꜱᴇ 🔐', url='https://youtu.be/2FHgg8o1YY8') ] ] ) )


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
