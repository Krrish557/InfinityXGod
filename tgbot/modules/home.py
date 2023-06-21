import time
from tgbot.modules.disable import DisableAbleCommandHandler
from tgbot.modules.helper_funcs.readable_time import get_readable_time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import CallbackContext, CallbackQueryHandler
from tgbot.vars import PM_START_TEXT, SUPPORT_CHAT
from tgbot import   StartTime, dispatcher,pbot
import tgbot.database.sql.users_sql as sql






    
def home_back(update: Update, context: CallbackContext):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ➕", url=f"t.me/{pbot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ], 
    ]
    query = update.callback_query
    if query and query.data == "home_":
        query.message.delete()
    first_name = update.effective_user.first_name
    uptime = get_readable_time((time.time() - StartTime))
    users = f"{sql.TOTAL_USERS}"
    chats = f"{sql.TOTAL_CHATS}"
    first_name = update.effective_user.first_name
    start_text = PM_START_TEXT.format(escape_markdown(first_name), pbot.first_name, users, chats, uptime)
            
    update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(buttons),
    parse_mode=ParseMode.MARKDOWN,)

      
    



home_handler = CallbackQueryHandler(
    home_back, pattern=r"home_", run_async=True
)

start_handler = DisableAbleCommandHandler("start", home_back, run_async=True)
dispatcher.add_handler(start_handler)

dispatcher.add_handler(home_handler)

