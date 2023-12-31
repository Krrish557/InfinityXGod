from redis import StrictRedis
from tgbot.vars import REDIS_URL
from tgbot import LOGGER

REDIS = StrictRedis.from_url(REDIS_URL,decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("Your redis server is now alive!")
except BaseException:
    raise Exception("Your redis server is not alive, please check again.")
    
