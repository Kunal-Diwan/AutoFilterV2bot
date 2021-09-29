# (c) @Kunal-Diwan & @MR_JINN_OF_TG

from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot.bot import Bot
from bot import FORCESUB_CHANNEL, ADMINS, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages

db = Database()

#=====================================================================================##



WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""


#=====================================================================================##

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>↗️ Join My Updates Channel To Use Me ↗️</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 🤭 JOIN OUR CHANNEL 🤭 ", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Head to @DevelopedBotz")
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption ="❤️ Thanks for using our bot . \n\n❁ 𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤 ❁  \n\n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n\n📌 Channel: @DevelopedBots \n👥 Group : @DevelopedBotz",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('↗️ Share ↗️', url="https://t.me/share/url?url=Hello+there+Subscribe+to+@DevelopedBots+for+various+types+of+Bots+🤖+🤖")
                ],
                [
                    InlineKeyboardButton('Channel 📢', url="https://t.me/DevelopedBots"),
                    InlineKeyboardButton('Support 💬', url="https://t.me/DevelopedBotz")
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('💻 Developer 💻', url="https://t.me/KunalDiwan")
                ],
                [
                    InlineKeyboardButton('Channel 📢', url="https://t.me/DevelopedBots"),
                    InlineKeyboardButton('Support 💬', url="https://t.me/DevelopedBotz")
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developer 👨‍🏭', url="https://t.me/kunaldiwan"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    await bot.send_photo(
        chat_id=update.chat.id,
        photo = 'https://telegra.ph/file/4e9baf69190f8a56482db.jpg',
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [

                [
                    InlineKeyboardButton('➕ Add me to Chat ➕', url='http://t.me/AutoFilterV2bot?startgroup=true')
                ],
                [
                    InlineKeyboardButton('📢 Updates 📢', url='https://t.me/DevelopedBots'),
                    InlineKeyboardButton('💬 Support 💬', url='https://t.me/DevelopedBotz')
                ],
                [
                    InlineKeyboardButton('🔒 Close 🔒', callback_data='close')
                ]
            ]
        ), 
        parse_mode="html", 
        reply_to_message_id=update.message_id
       )
    await bot.send_message(
		update.chat.id,
		'Use below buttons to interact with me',
		reply_markup=ReplyKeyboardMarkup(
			[
				['🤖 About 🤖','⚙️ Help ⚙️']
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
	)


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('❓ About❓', callback_data='about'),
        InlineKeyboardButton('🔐 Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & (filters.private | filters.group), group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('🔐 Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["source"]) & (filters.private | filters.group), group=1)
async def source(bot, update):
    buttons = [[
        InlineKeyboardButton('💻 Source 💻', url='https://github.com/Kunal-Diwan/AutoFilterV2bot'),
        InlineKeyboardButton('🔐 Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SOURCE_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.regex(r'^🤖 About 🤖$'))
async def _manage(_, msg):
    text=Translation.KBDABOUT_TEXT
    text += "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    await msg.reply(
        text,
        reply_markup=ReplyKeyboardMarkup(
			[
				['⬅️ Back','👨‍💻 Developer 👨‍💻']
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
	)

@Client.on_message(filters.regex(r'^⬅️ Back$'))
async def _manage(_, msg):
    await bot.send_text(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=ReplyKeyboardMarkup(
			[
				['🤖 About 🤖','⚙️ Help ⚙️']
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
	)
