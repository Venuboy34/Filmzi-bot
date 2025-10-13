import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = 'FilmziMovieBot'   # Session name for the bot
API_ID = 20288994  # API ID from my.telegram.org
API_HASH = 'd702614912f1ad370a0d18786002adbf'  # API Hash from my.telegram.org
BOT_TOKEN = '8416909627:AAFbJM9nQtqqttTnuN1KOkRScR6Fa_Z6cLQ'    # Bot token from @BotFather

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = 300    # Cache time in seconds (default: 5 minutes)
USE_CAPTION_FILTER = True  # Use caption filter for search results
INDEX_CAPTION = True # Save caption db when indexing

PICS = ['https://graph.org/file/246a70cb4387b59cceb15-9e968f8602a6acb36c.jpg']  # Sample pic
NOR_IMG = "https://graph.org/file/e20b5fdaf217252964202.jpg"
MELCOW_PHOTO = "https://graph.org/file/56b5deb73f3b132e2bb73.jpg"
SPELL_IMG = "https://graph.org/file/13702ae26fb05df52667c.jpg"
SUBSCRIPTION = 'https://graph.org/file/242b7f1b52743938d81f1.jpg'
FSUB_PICS = ['https://graph.org/file/e98dbe89391356a940db5-dbf10e15e03e1ed77a.jpg']  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [8304706556] # Admin ID(s)
CHANNELS = [-1002897456594]  # Channel id for auto indexing

LOG_CHANNEL = -1002995694885  # Log channel id (updated)
BIN_CHANNEL = -1002897456594  # Bin channel id
PREMIUM_LOGS = -1002995694885  # Premium logs channel id (updated)
DELETE_CHANNELS = [-1002897456594] 
support_chat_id = -1002897456594  # Support group id
reqst_channel = -1002897456594  # Request channel id
SUPPORT_CHAT = 'https://t.me/filmzi_support'  # Support group link (updated)

# FORCE_SUB 
auth_req_channel = -1002897456594  # Channel for force sub
AUTH_CHANNELS = [-1002897456594]  # Channels for force sub

# ============================
# Payment Configuration
# ============================
QR_CODE = 'https://graph.org/file/1b2471aaeb5a7f4bb5266-cddfd202f6de756926.jpg'    # QR code image for payments
OWNER_UPI_ID = 'ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ'    # Owner UPI ID for payments

STAR_PREMIUM_PLANS = {
    10: "7day",
    20: "15day",    
    40: "1month", 
    55: "45day",
    75: "60day",
}  # Premium plans with their respective durations in days

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = "mongodb+srv://moviedatabase:venura%408907@cluster0.hg0etvt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # MongoDB URI for the database
DATABASE_NAME = "Cluster0" # Database name
COLLECTION_NAME = 'Filmzi_Files' # Collection name

# Multiple DB Configuration
MULTIPLE_DB = False # Set to False for single database
DATABASE_URI2 = DATABASE_URI  # Same as primary database

# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = True  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = -1002897456594  # Notification channel
FILMZI_IMAGE_FETCH = True  # On (True) / Off (False) - Updated from DREAMXBOTZ
LINK_PREVIEW = False # Shows link preview in notification msg instead of image
ABOVE_PREVIEW = True # Shows link preview above the text in notification msg
TMDB_API_KEY = '282fec93f7dac5a152e0b321327b46c4' # TMDB API Key
TMDB_POSTER = True # Shows TMDB poster in notification msg
LANDSCAPE_POSTER = True # Shows landscape poster in notification msg

# ============================
# Verification Settings
# ============================
IS_VERIFY = False  # Verification On (True) / Off (False)
LOG_VR_CHANNEL = -1002995694885 #Verification Channel Id (updated)
LOG_API_CHANNEL = -1002995694885 #API Channel Id (updated)
VERIFY_IMG = "https://graph.org/file/d7a2ec5a7343175789cbb-ce6b1d2e43103b5b20.jpg"

TUTORIAL = "https://t.me/filmzi_updates"   # Tutorial link for verification (updated)
TUTORIAL_2 = "https://t.me/filmzi_support"   # Second tutorial link (updated)
TUTORIAL_3 = "https://t.me/Zeroboy216"   # Third tutorial link

# Verification Shortener Settings
SHORTENER_API = "a7ac9b3012c67d7491414cf272d82593c75f6cbb" # Shortener API key
SHORTENER_WEBSITE = "omegalinks.in" # Shortener website

SHORTENER_API2 = "a7ac9b3012c67d7491414cf272d82593c75f6cbb"  # Shortener API key for second website
SHORTENER_WEBSITE2 = "omegalinks.in" # Shortener website for second website

SHORTENER_API3 = "a7ac9b3012c67d7491414cf272d82593c75f6cbb"  
SHORTENER_WEBSITE3 = "omegalinks.in" # Shortener website for third website

TWO_VERIFY_GAP = 1200 # Time gap for two-step verification in seconds
THREE_VERIFY_GAP = 54000    

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = 'https://t.me/filmzi_community' # Group link for the bot (updated)
OWNER_LNK = 'https://t.me/Zeroboy216' # Owner link for the bot
UPDATE_CHNL_LNK = 'https://t.me/filmzi_updates' # Update channel link for the bot (updated)

# ============================
# User Configuration
# ============================
auth_users = [8304706556]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [8304706556]

# ============================
# Miscellaneous Configuration
# ============================
MAX_B_TN = "5" # Maximum number of buttons in a row
PORT = "8080"  # Port for the web server
MSG_ALRT = '🎬 Thanks for using Filmzi! Share with friends! 🍿' # Alert message for users (updated)
DELETE_TIME = 300  # Deletion time in seconds
CUSTOM_FILE_CAPTION = f"{script.CAPTION}"   # Custom caption for files
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION # Custom caption for batch files
IMDB_TEMPLATE = f"{script.IMDB_TEMPLATE_TXT}"     # Custom IMDB template 
MAX_LIST_ELM = None # Maximum number of elements in a list
INDEX_REQ_CHANNEL = LOG_CHANNEL  # Index Request Channel ID
NO_RESULTS_MSG = True  # True if you want no results messages in Log Channel
MAX_BTN = True    # Max Button On (True) / Off (False)
P_TTI_SHOW_OFF = False    # P_TTI_SHOW_OFF On (True) / Off (False)
IMDB = False    # IMDB Results On (True) / Off (False)
AUTO_FFILTER = True # Auto Filter On (True) / Off (False)
AUTO_DELETE = True # Auto Delete On (True) / Off (False)
LONG_IMDB_DESCRIPTION = False # Long IMDB Description On (True) / Off (False)
SPELL_CHECK_REPLY = True # Spell Check Mode On (True) / Off (False)
MELCOW_NEW_USERS = False # Melcow New Users On (True) / Off (False)
PROTECT_CONTENT = False # Protect Content On (True) / Off (False)
PM_SEARCH = True  # PM Search On (True) / Off (False)
EMOJI_MODE = True  # Emoji status On (True) / Off (False)
BUTTON_MODE = True # pm & Group button or link mode (True) / Off (False)
STREAM_MODE = True # Set Stream mode True or False

# ============================
# Bot Configuration
# ============================
AUTH_REQ_CHANNEL = auth_req_channel
REQST_CHANNEL = reqst_channel
SUPPORT_CHAT_ID = support_chat_id
LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

SEASON_COUNT = 12
SEASONS = [f"S{str(i).zfill(2)}" for i in range(1, SEASON_COUNT + 1)]

BAD_WORDS = {
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2",
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "primefix",
} # Set of bad words to filter out

# ============================
# Server & Web Configuration
# ============================
NO_PORT = False
APP_NAME = None

# Fix for the environ error - check if we're on Heroku/Koyeb
ON_HEROKU = False
if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = os.environ.get('APP_NAME')
else:
    ON_HEROKU = False

BIND_ADRESS = '0.0.0.0'
FQDN = BIND_ADRESS if not ON_HEROKU or os.getenv('FQDN') else APP_NAME+'.herokuapp.com'

# Fix URL construction
if ON_HEROKU or NO_PORT:
    URL = f"https://{FQDN}/"
else:
    URL = f"https://{FQDN}:{PORT}/"

SLEEP_THRESHOLD = 60
WORKERS = 4
SESSION_NAME = 'FilmziMovieBot'
MULTI_CLIENT = False
name = 'FilmziMovieBot'
PING_INTERVAL = 1200  # 20 minutes

# Fix the second ON_HEROKU check
if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = 'FilmziMovieBot'
else:
    ON_HEROKU = False

HAS_SSL = True
if HAS_SSL:
    URL = f"https://{FQDN}/"
else:
    URL = f"http://{FQDN}/"

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Command Bot
# ============================
Bot_cmds = {
    "start": "🎬 Start Filmzi Bot",
    "stats": "📊 Get Bot Statistics",
    "alive": "💚 Check Bot Status",
    "settings": "⚙️ Change Settings",
    "id": "🆔 Get Telegram ID",
    "info": "👤 Get User Info",
    "del_msg": "🗑️ Remove File Notifications",
    "movie_update": "🔔 Movie Updates On/Off",
    "pm_search": "🔍 PM Search On/Off",
    "trendlist": "📈 Top Trending Searches",
    "broadcast": "📢 Broadcast to Users",
    "grp_broadcast": "📢 Broadcast to Groups",
    "send": "📨 Send Message to User",
    "add_premium": "⭐ Add Premium User",
    "remove_premium": "⭐ Remove Premium User",
    "premium_users": "⭐ Premium Users List",
    "restart": "🔄 Restart Bot",
    "group_cmd": "📋 Group Commands",
    "admin_cmd": "👑 Admin Commands"
}

#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2

# ============================
# Logs Configuration
# ============================
LOG_STR = "🎬 Filmzi Movie Bot - Current Configuration:\n"
LOG_STR += ("✅ IMDB Results enabled\n" if IMDB else "❌ IMDB Results disabled\n")
LOG_STR += ("✅ P_TTI_SHOW_OFF enabled - Users redirected to /start\n" if P_TTI_SHOW_OFF else "❌ P_TTI_SHOW_OFF disabled - Files sent directly\n")
LOG_STR += ("✅ BUTTON_MODE enabled - Single button layout\n" if BUTTON_MODE else "❌ BUTTON_MODE disabled - Dual button layout\n")
LOG_STR += (f"✅ Custom caption enabled\n" if CUSTOM_FILE_CAPTION else "❌ No custom caption - Using defaults\n")
LOG_STR += ("✅ Long IMDB descriptions enabled\n" if LONG_IMDB_DESCRIPTION else "❌ Short IMDB descriptions\n")
LOG_STR += ("✅ Spell Check enabled\n" if SPELL_CHECK_REPLY else "❌ Spell Check disabled\n")
