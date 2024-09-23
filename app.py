from config import app_config

print(">>>>")

if app_config.db_user == "":
    raise Exception("FATAL")

