from pyrogram import Client, idle

from tgbot.vars import API_HASH, API_ID, TOKEN


class Bot(Client):
    def __init__(self) -> None:
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins={"root": "tgbot.modules"}
        )


    def start(self):
        super().start()
        get_me = self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.first_name = get_me.first_name
        self.last_name = get_me.last_name
