from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "418866e765a1494d4aaade9282c9470e")
      API_ID = int(getenv("API_ID", "24155199"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6736421654:AAHNHFh1DGZJq4wtephlq8mcYqZOtwbd1Rg")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001883240370:-1001973699665").replace("\n", " ").split(' '))
      

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
