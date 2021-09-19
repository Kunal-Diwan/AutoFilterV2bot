from pyrogram.handlers import InlineQueryHandler
from youtubesearchpython import VideosSearch
from utils import USERNAME
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
from pyrogram import Client, errors
from bot import bot
REPLY_MESSAGE=Config.REPLY_MESSAGE

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "KOUTHUKAM_LESHAM_KOODUTHALA":
        answers.append(
            InlineQueryResultPhoto(
                    title="do you wanna help huh?",
                    thumb_url="https://telegra.ph/file/4e9baf69190f8a56482db.jpg",
                    photo_url="https://telegra.ph/file/4e9baf69190f8a56482db.jpg",
                    caption=(f"{REPLY_MESSAGE}\n\n**Powered By** [ __@KunalDiwan | @DevelopedBots__ ]"),
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "/p https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("Nothing found"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
