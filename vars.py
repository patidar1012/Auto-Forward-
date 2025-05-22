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

SESSION = environ.get("SESSION", "forward bot")
API_ID = 25163484
API_HASH = "145bcbc424d1c1ffe04f3e607ea55c9a"
BOT_TOKEN = environ.get("BOT_TOKEN")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002137528664"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6302921275').split()]
FROM_DB = int(environ.get("FROM_DB", "-1002369988753"))
TARGET_DB = int(environ.get("TARGET_DB", "-1002399329080"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MandaliWala/File-Forward-Bottermux")
