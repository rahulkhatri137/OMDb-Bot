from asyncio import sleep
from OMDB import get_movie_info
from info import API_ID, BOT_TOKEN, API_HASH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


START_MSG = "𝖧𝖺𝗂 <b>{}</b>, \n𝖨'𝗆 𝖺 𝖲𝗂𝗆𝗉𝗅𝖾 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 𝖳𝗈 𝖦𝖾𝗍 𝖬𝗈𝗏𝗂𝖾 𝖨𝗇𝖿𝗈 𝖴𝗌𝗂𝗇𝗀 𝖮𝖬𝖣𝖻\n \n𝖲𝖾𝗇𝖽 𝖬𝖾 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖨𝗇𝖿𝗈 𝖠𝖻𝗈𝗎𝗍 𝖨𝗍"
STICKER = 'CAACAgUAAxkDAALjS2F9dI-C4OaXKkSgsAxjX1mkofkKAAJXBAAC6aXoV2X6ud6KqXzUHgQ'  


Bot = Client(
    session_name="OMDb-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@Bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_sticker(STICKER)
    await message.reply_text(START_MSG.format(message.from_user.mention))
               
@Bot.on_message(filters.text)
async def search(client, message):
    movie_name = message.text.replace(" ", "+")
    try:
        poster, id, text = get_movie_info(movie_name)
        buttons=[[InlineKeyboardButton('🎟 𝖨𝖬𝖣𝖻', url=f"https://www.imdb.com/title/{id}")]]    
        m=await message.reply_text("𝖥𝗂𝗇𝖽𝗂𝗇𝗀 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
        await message.reply_photo(photo=poster.replace("SX300",""), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
        await m.delete()                                                          
    except ValueError:
        m=await message.reply_text("𝖲𝗈𝗋𝗋𝗒,\n𝖨 𝖢𝖺𝗇'𝗍 𝖥𝗂𝗇𝖽 𝖯𝗈𝗌𝗍𝖾𝗋𝗌.\n𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(4)
        await m.delete()
    except Exception as e:
        buttons=[[InlineKeyboardButton('🔍 𝖲𝖾𝖺𝗋𝖼𝗁 𝖮𝗇 𝖦𝗈𝗈𝗀𝗅𝖾.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="𝖢𝗈𝗎𝗅𝖽𝗇'𝗍 𝖥𝖾𝗍𝖼𝗁 𝖣𝖾𝗍𝖺𝗂𝗅𝗌\n𝖳𝗋𝗒 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 yo𝗎𝗋 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀.", reply_markup=InlineKeyboardMarkup(buttons))  
        await m.delete()   
        print(e)   
                                                                   
print("Bot Started!")

Bot.run()

# ariyavunna pole cheythittund 😒
