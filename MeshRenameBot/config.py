from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://Nons:Nons@cluster0.eeydztb.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "908e8bff7c8f6ecd5d0ab989f78134fc"]
        API_ID = [int, 9830058]
        BOT_TOKEN = [str, "6055223043:AAE4yj8Tptg2vCCQfsw5HAB3cA0tc_ZTsr4"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[5572938538]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/mohanishx"]
        FORCEJOIN_ID = [int,--1001942001094]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
