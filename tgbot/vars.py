import os
from dotenv import load_dotenv
load_dotenv()

# Bot
TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
WORKERS = int(os.environ.get("WORKERS", 8))

if TOKEN == "":
    raise ValueError("BOT_TOKEN is missing in the environment variables.")

if API_ID == "":
    raise ValueError("API_ID is missing in the environment variables.")

if API_HASH == "":
    raise ValueError("API_HASH is missing in the environment variables.")

# Sudo
try:
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
except ValueError:
    raise Exception("Your OWNER_ID env variable is provided or is not a valid integer.")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

try:
    DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
except ValueError:
    raise Exception("Your dev users list does not contain valid integers.")
try:
    SUDOS = set(int(x) for x in os.environ.get("SUDOS", "").split())
except ValueError:
    raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
    HELPERS = set(int(x) for x in os.environ.get("HELPERS", "").split())
except ValueError:
    raise Exception("Your support users list does not contain valid integers.")


# Database
DB_URL = os.environ.get("DATABASE_URL", "")
if DB_URL == "":
    raise ValueError("DATABASE_URL is missing in the environment variables.")
DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")
if MONGO_DB_URI == "":
    raise ValueError("MONGO_DB_URI is missing in the environment variables.")

REDIS_URL = os.environ.get("REDIS_URL", "")
if REDIS_URL == "":
    raise ValueError("REDIS_URL is missing in the environment variables.")


# API Keys
CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
AI_API_KEY = os.environ.get("AI_API_KEY", None)
API_WEATHER = os.environ.get("API_WEATHER", None)
WALL_API = os.environ.get("WALL_API", None)
APOD_API_KEY = os.environ.get("APOD_API_KEY", None)
ARQ_API_KEY = os.environ.get("ARQ_API", None)


# Misc
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)

try:
    WHITELIST_CHATS = {int(x) for x in os.environ.get('WHITELIST_CHATS', "").split()}
except ValueError:
    raise Exception(
        "Your blacklisted chats list does not contain valid integers.")

try:
    BLACKLIST_CHATS = {int(x) for x in os.environ.get('BLACKLIST_CHATS', "").split()}
except ValueError:
    raise Exception(
        "Your blacklisted chats list does not contain valid integers.")


            
PM_START_TEXT = """
════════《✧》════════
𝙺𝚘𝚗𝚗𝚒𝚌𝚑𝚒𝚠𝚊 *{} - 𝚜𝚊𝚗*

𝙸 𝚊𝚖 *{}*, 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚖𝚊𝚗𝚊𝚐𝚎𝚖𝚎𝚗𝚝 𝚋𝚘𝚝.
════════════════
♡ 𝐔𝐬𝐞𝐫𝐬: `{}`
♡ 𝐂𝐡𝐚𝐭𝐬: `{}`
♡ 𝐔𝐩𝐭𝐢𝐦𝐞: `{}`
════════════════
𝚄𝚜𝚎 /help 𝚝𝚘 𝚐𝚘 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚖𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜.
════════《✧》════════
"""

HELP_STRINGS = """
𝙲𝚕𝚒𝚌𝚔 𝚘𝚗 𝚝𝚑𝚎 𝚋𝚞𝚝𝚝𝚘𝚗 𝚋𝚎𝚕𝚕𝚘𝚠 𝚝𝚘 𝚐𝚎𝚝 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚜𝚙𝚎𝚌𝚒𝚏𝚒𝚌𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍."""
