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
API_ID = 24770554
API_HASH = "6f17857655c644baed6ecca72bbce7f6"
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6571116013').split()]
TARGET_DB = int(environ.get("TARGET_DB", "-1002222465571"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/patidar1012/Auto-Forward-.git")
#Auto Forward vars
FROM_DB = [int(channel_id) for channel_id in environ.get('FROM_DB', '-1002552806781 -1002031007752 -1001676473152 -1001307877241 -1002565856677 -1003381764555 -1003127045372').split() if re.match(r'^-?\d+$', channel_id)]
TO_DB = int(environ.get("TO_DB", "-1002222465571"))








