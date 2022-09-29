## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCNHjCO7G4DBWSg8REFXiH2Zq6syPVSx8m-q5fhID9LwDUiJMQaWqmBLvFo_6EtrCMTQzayWgn2W3JcxuHm2R-k7eBVoBSbFEXLgHBVH6SjhaFzfCgZRroup6CK1ERiCucEKmQDMBGgh0fTMlK-CWdDVUNDUjVnoBpCah4zRVVheZEX7Nu8dhzyzHfbvy2rCewJ485VxV6Gsi2zNJz6wPf0R0FP4Hgqgv38yC6qHyBl0KZR6SlAP16d0xQ_5Lwz2pkWy03pTdqwJnG8ugNL8uN4s_i_Smj_fIvodsybIwifP1lbPx7OllRFuPvhlh1Jo3zwEWwIon6RlGK_4dTpXM5CAAAAAUogW0cA")
BOT_TOKEN = getenv("BOT_TOKEN", "5777428524:AAEGoDCWKuz_Qth_yarrt0-UfnEE-q4G4-Q")
BOT_NAME = getenv("BOT_NAME", "Music kaisel")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", ". 22 .")
OWNER_USERNAME = getenv("OWNER_USERNAME", "RQWRR")
ALIVE_NAME = getenv("ALIVE_NAME", " .22.")
BOT_USERNAME = getenv("BOT_USERNAME", "@Teamkaiselbot")
OWNER_ID = getenv("OWNER_ID", "5564868491")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@llfIPN")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@Teamkaisel")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5564868491").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
