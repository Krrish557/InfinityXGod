
import asyncio
import importlib
from sys import argv
from tgbot.database.sql.users_sql import ensure_bot_in_db
from tgbot.vars import (

    SUPPORT_CHAT,
    TOKEN,
 )
from tgbot import(
    LOGGER,
    dispatcher,
    telethn,
    pbot,
    updater,
    IMPORTED,
MIGRATEABLE,
HELPABLE,
STATS,
USER_INFO,
DATA_IMPORT,
DATA_EXPORT,
CHAT_SETTINGS,
USER_SETTINGS,
)


from tgbot.modules import ALL_MODULES
from telegram import Chat, ParseMode, Update, Message
from telegram.error import (
    BadRequest,
    Unauthorized,
)

from telegram.ext.dispatcher import DispatcherHandlerStop
from pyrogram import idle
bot_name = f"{dispatcher.bot.first_name}"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



for module_name in ALL_MODULES:
    imported_module = importlib.import_module("tgbot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


def main():
    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            msg = dispatcher.bot.send_message(
            f"@{SUPPORT_CHAT}",
            "👋 Hi, i'm alive.",
            parse_mode=ParseMode.MARKDOWN
            )
            try:
                msg.delete()
            except BadRequest:
                LOGGER.critical("Bot was not able to delete message in support chat [@{}].".format(SUPPORT_CHAT))
        except Unauthorized:
            LOGGER.warning(
                "Bot isnt able to send message to support_chat [@{}].".format(SUPPORT_CHAT) + ", go and check!"
            )
        except BadRequest as e:
            LOGGER.warning(e.message)   

    LOGGER.info("Using long polling.")
    updater.start_polling(timeout=15, read_latency=0.01, drop_pending_updates=True)


    ensure_bot_in_db()
    
    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()
    
    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
    LOGGER.info("Bot Started")

