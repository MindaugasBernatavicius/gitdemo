from config import app_config
from requests import get

res = get("https://delfi.lt")

if app_config.db_user == "":
    raise Exception("FATAL")
else:
    raise Exception
