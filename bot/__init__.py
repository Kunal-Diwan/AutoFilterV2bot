#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

#force sub config

FORCESUB_CHANNEL = os.environ.get("FORCESUB_CHANNEL", "")

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID"))

API_HASH = os.environ.get("API_HASH")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "737063440"))

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append("OWNER_ID")
ADMINS.append(1701601729)

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
