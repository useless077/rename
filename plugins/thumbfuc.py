from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb
from config import Config

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
		thumb = find(int(message.chat.id))
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**You dont have any custom Thumbnail**")
	
	
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Custom Thumbnail Deleted Successfully**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
	
# dummy 

@Client.on_message(filters.photo & filters.incoming & filters.private)
async def save_photo(c, m):

    download_location = f"{Config.DOWNLOAD_LOCATION}/{m.from_user.id}.jpg"
    await update_thumb(m.from_user.id, m.message_id)
    await m.download(file_name=download_location)

    await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
