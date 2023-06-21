import logging
import os
import sys
import time

from tgbot.bot import Bot
# from tgbot.database.sql.users_sql import num_chats, num_users
# from tgbot.utils.interval import set_interval

from tgbot.vars import OWNER_ID, DEV_USERS, HELPERS, SUDOS, TOKEN, WORKERS, API_HASH, API_ID, ARQ_API_KEY
from pyrogram import Client, filters
from aiohttp import ClientSession
import telegram.ext as tg
from telethon import TelegramClient
from Python_ARQ import ARQ
from telethon.sessions import MemorySession

StartTime = time.time()

# enable logging
if os.path.exists("bot_logs.txt"):
    os.remove("bot_logs.txt")

FORMAT = "[tgbot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[tgbot]')
LOGGER.info("tgbot is starting. | Built by SOME1HING.")
LOGGER.info("Handled by: github.com/SOME-1HING (t.me/SOME1HING)")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Aiohttp Client
aiohttpsession = ClientSession()
session = ClientSession()

# ARQ Client
arq = ARQ("https://arq.hamker.in", ARQ_API_KEY, session)

# Pyrogram CLient
pbot = Bot()

# PTB Client
defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher

# Telethon Client
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

# Updating Sudo list
DEV_USERS.add(OWNER_ID)
SUDOERS = filters.user()
SUDOS = list(SUDOS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
HELPERS = list(HELPERS)



# Load at end to ensure all prev variables have been set
from tgbot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler


