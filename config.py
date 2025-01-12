# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24519654"))
API_HASH = getenv("API_HASH", "1ccea9c29a420df6a6622383fbd83bcd")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1114789110").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1004739998812")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002394679447"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "9000"))
WEBSITE_URL = getenv("WEBSITE_URL", "krownlinks.com")
AD_API = getenv("AD_API", "4dbeb3373153a8396dd23d2e9da53c8f24f4b449")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
