from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "")
      API_ID = int(getenv("API_ID", ""))
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      AS_COPY = True if getenv("AS_COPY", True) #== "`{defult}`" else True
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
      

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
