#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @kunaldiwan

class Translation(object):
    
    START_TEXT = """<b>Hello {} - I'm Auto filter V2 Bot .

I can help you to filter files automatically from channel to group .

โก๏ธ Just add me to your group and channel as admin .

For more details hit /help ....

Powered by @DevelopedBots ๐
</b>"""    
    
    HELP_TEXT = """
<b>Hi , I am Auto filter Bot V2 . I can help you to filter files .</b>

<b><u>Helpful commands ๐</u></b>

ยปยป <code>/about</code> - Check about me ...

ยปยป <code>/source</code> - Get details about my source

ยปยป <code>/add chat_id</code> - To connect a group with a channel .

ยปยป <code>/dell chat_id</code> - To disconnect a group with a channel.

ยปยป <code>/delall</code> - This command will disconnect all connected channel with the group and deletes all its file from DB .

โ ๏ธ Bot should be admin in both channel and group .

<b>If you got any issues about Bot ask at @DevelopedBotz .</b>
"""
    
    ABOUT_TEXT = """<b>โฅ ๐ค Name</b> : <code> Auto Filter V2 Bot</code>
    
<b>โฅ ๐จโ๐ป Creator</b> : <b><a href="https://t.me/kunaldiwan">Kunal diwan</a></b>

<b>โฅ ๐ณโ๐ Language</b> : <code>Python3</code>

<b>โฅ ๐ Library</b> : <a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a>

โโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
"""

    KBDABOUT_TEXT = """<b>โฅ ๐ค Name</b> : <code> Auto Filter V2 Bot</code>
    
<b>โฅ ๐จโ๐ป Creator</b> : <b>@KunalDiwan</b>

<b>โฅ ๐ณโ๐ Language</b> : <code>Python3</code>

<b>โฅ ๐ Library</b> : <a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a>

"""
    
    SOURCE_TEXT = """Oh you want my source . I am built in python 3, Using the Pyrogram library, and am fully open source .

Don't forgot to fork ๐ด and star ๐ the repo . 

Check my source below ๐
"""
