from typing import Optional

from tgbot import(
    LOGGER,
    MIGRATEABLE,
    dispatcher,

)


from telegram import  Update, Message

from telegram.ext import (
    CallbackContext,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop
def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop

migrate_handler = MessageHandler(
    Filters.status_update.migrate, migrate_chats, run_async=True
)

dispatcher.add_handler(migrate_handler)