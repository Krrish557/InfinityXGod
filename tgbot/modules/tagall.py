

from tgbot import telethn
from tgbot.events import register


@register(pattern="^(/all|/mentionall|/tagall|/utag|@all|@mentionall|@tagall|@utag) ?(.*)")
async def _(event):
    if not event.is_group:
        return
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 99999999):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        try:
            await event.send_message(event.chat_id, mentions, reply_to=event.reply_to_msg_id)
        except:
            await event.reply(mentions)
    await event.reply(mentions)

__mod_name__ = "TagAll"
__help__ = """
*Tag All*
 ❍ `/users` : Get txt file of all users in your group.
 ❍ `/all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
"""
