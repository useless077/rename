from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 
from Script import script

@Client.on_message(filters.command(["start"]))
async def start(client, message):
          await client.send_message(
          chat_id=message.chat.id,
          text=script.START_TEXT.format(user_mention=message.from_user.mention),
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='⭕ Cʜᴀɴɴᴇʟ ⭕', url=f'https://t.me/TamilBots'),
                                                 InlineKeyboardButton(text='⭕ Sᴜᴘᴘᴏʀᴛ ⭕', url=f'https://t.me/TamilBots') ],
                                               [ InlineKeyboardButton(text='👨‍💻 Dᴇᴘʟᴏʏ Nᴏᴡ', url='https://youtube.com/c/TamilBots'),                                                
                                                 InlineKeyboardButton(text='🔐 Cʟᴏꜱᴇ 🔐', url='https://youtube.com/c/TamilBots') ] ] ) )
@Client.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(c, m, cb=False):
    me = await c.get_me()
    button = [[
        InlineKeyboardButton(text='🏡Home', callback_data='back'),
        InlineKeyboardButton(text='🚪Close', callback_data="close")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await m.message.edit(
            text=TEXT.ABOUT.format(bot_name=me.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await m.reply_text(
            text=TEXT.ABOUT.format(bot_name=me.mention),            
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
