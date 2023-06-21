

from . import db

aservice = db.aservice

def is_aservice(chat_id: int) -> bool:
    chat = aservice.find_one({"chat_id": chat_id})
    if chat:
        return True
    return False

def set_aservice(chat_id):
    aservice = aservice(chat_id)
    if aservice:
        return
    return aservice.insert_one({"chat_id": chat_id})

def rem_aservice(chat_id):
    aservice = aservice(chat_id)
    if not aservice:
        return
    return aservice.delete_one({"chat_id": chat_id})