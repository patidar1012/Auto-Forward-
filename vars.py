from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "N2 forward bot")
USER_SESSION = environ.get("USER_SESSION", "") #Pyrogram session dalna hai yahan
API_ID = 25163484
API_HASH = "145bcbc424d1c1ffe04f3e607ea55c9a"
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002137528664"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6302921275').split()]
TARGET_DB = int(environ.get("TARGET_DB", "-1002155536121"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MandaliWala/File-Forward-Bottermux")
#Auto Forward vars
FROM_DB = [int(channel_id) for channel_id in environ.get('FROM_DB', '-1002248826741 -1002116767957 -1002464939396 -1002753463498 -1001971879597 -1002510094945 -1002056617893 -1002369988753').split() if re.match(r'^-?\d+$', channel_id)]
TO_DB = int(environ.get("TO_DB", "-1002189644835"))
