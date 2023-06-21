import asyncio
import sys

from motor import motor_asyncio
from tgbot import LOGGER
from tgbot.vars import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


client = MongoClient(MONGO_DB_URI)
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
db = client["TgBot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(LOGGER.critical("Can't connect to mongodb! Exiting..."))
