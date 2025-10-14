class script(object):
    START_TXT = """
╔════════ ≪ °❈° ≫ ════════╗

<b>🎬 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗙𝗶𝗹𝗺𝘇𝗶 𝗠𝗼𝘃𝗶𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿! 🎭</b>

<b>👋 𝗛𝗲𝘆 {}! 𝗥𝗲𝗮𝗱𝘆 𝘁𝗼 𝗱𝗶𝘀𝗰𝗼𝘃𝗲𝗿 𝗮𝗺𝗮𝘇𝗶𝗻𝗴 𝗺𝗼𝘃𝗶𝗲𝘀? 🍿</b>

╚════════ ≪ °❈° ≫ ════════╝

<b>🔍 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗮𝗱𝗲 𝗘𝗮𝘀𝘆:</b>
• Just type any <b>Movie Name</b> or <b>WebSeries Title</b>
• Use proper <b><a href='https://www.google.com/'>Google</a> spelling</b>
• Get instant download links! ⚡</b>"""
    
    GSTART_TXT = """🎬 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗙𝗶𝗹𝗺𝘇𝗶 𝗠𝗼𝘃𝗶𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿! 🎭"""
    
    HELP_TXT = """<b>
╔════════ ≪ °❈° ≫ ════════╗
         🎯 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 🎯
╚════════ ≪ °❈° ≫ ════════╝

📝 <b>Search Format Guidelines:</b>

🎥 <u>Movie Examples</u>:
┣✦ Avatar
┣✦ Avatar 2009
┣✦ The Dark Knight
┗✦ The Dark Knight 2008

📺 <u>WebSeries Examples</u>:
┣✦ Game of Thrones
┣✦ Game of Thrones S01
┣✦ Money Heist
┗✦ Money Heist S02 E05

⚠️ <b>Important Notes:</b>
• Use letters only - no emojis ❌
• Correct spelling is crucial ✅
• Include year for better results 📅
• Be specific with season/episode</b>"""

    ABOUT_TXT = """<b>╔════════ ≪ °❈° ≫ ════════╗
         🤖 𝗕𝗼𝘁 𝗗𝗲𝘁𝗮𝗶𝗹𝘀 🤖
╚════════ ≪ °❈° ≫ ════════╝

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  🎬 𝗙𝗶𝗹𝗺𝘇𝗶 𝗠𝗼𝘃𝗶𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├🔹 <b>Bot Name</b> : <a href=https://t.me/{}>{}</a>
├🔹 <b>Developer</b> : <a href={}>ZeroDev</a> 
├🔹 <b>Library</b> : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
├🔹 <b>Language</b> : <a href='https://www.python.org/'>Python 3</a> 
├🔹 <b>Database</b> : <a href='https://www.mongodb.com/'>Mongo DB</a> 
├🔹 <b>Server</b> : <a href='https://heroku.com/'>Heroku</a> 
├🔹 <b>Version</b> : v2.4 [ Stable ]
└🔹 <b>Status</b> : 🟢 Online</b>"""
    
    RESTART_TXT = """
╔════════ ≪ °❈° ≫ ════════╗
      🔄 𝗦𝘆𝘀𝘁𝗲𝗺 𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗲𝗱 🔄
╚════════ ≪ °❈° ≫ ════════╝

<b>🤖 Bot: {}</b>

📊 <b>System Status:</b>
├📅 <b>Date</b> : <code>{}</code>
├⏰ <b>Time</b> : <code>{}</code>
├🌐 <b>Timezone</b> : <code>Asia/Kolkata</code>
├🛠️ <b>Version</b> : v1.4 [ Stable ]
└🔧 <b>Status</b> : 🟢 Operational
</b>"""

    CHANNELS = """
╔════════ ≪ °❈° ≫ ════════╗
     📡 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 & 𝗚𝗿𝗼𝘂𝗽𝘀 📡
╚════════ ≪ °❈° ≫ ════════╝

<b>🌟 Premium Features:</b>
• Latest Movies & Series 🎬
• Super Fast Bots ⚡
• Free & Easy to Use 🆓
• 24/7 Active Service 🌙
• High Quality Content 🎯
• Instant Updates 🔔</b>"""

    MULTI_STATUS_TXT = """<b>╔════════ ≪ °❈° ≫ ════════╗
         📊 𝗦𝘆𝘀𝘁𝗲𝗺 𝗦𝘁𝗮𝘁𝘂𝘀 📊
╚════════ ≪ °❈° ≫ ════════╝

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      🗃️ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝟭      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├👥 Total Users: <code>{}</code>
├👥 Total Groups: <code>{}</code>
├⭐ Premium Users: <code>{}</code>
├📁 Total Files: <code>{}</code>
├💾 Used Storage: <code>{}</code>
├🆓 Free Storage: <code>{}</code>

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      🗳️ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝟮      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├📁 Total Files: <code>{}</code>
├📦 Total Size: <code>{}</code>
├🆓 Free Space: <code>{}</code>

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      🤖 𝗕𝗼𝘁 𝗜𝗻𝗳𝗼       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├⏰ Uptime: {}
├🧠 RAM Usage: <code>{}%</code>
├⚡ CPU Usage: <code>{}%</code>
├📊 Total DB Files: <code>{}</code>
└🔧 Status: 🟢 Running</b>"""

    STATUS_TXT = """<b>╔════════ ≪ °❈° ≫ ════════╗
         📈 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀 📈
╚════════ ≪ °❈° ≫ ════════╝

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      📊 𝗦𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├👥 Total Users: <code>{}</code>
├👥 Total Groups: <code>{}</code>
├⭐ Premium Users: <code>{}</code>
├📁 Total Files: <code>{}</code>
├💾 Used Storage: <code>{}</code>
├🆓 Free Storage: <code>{}</code>

┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      🖥️ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗜𝗻𝗳𝗼     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛

├⏰ Uptime: {}
├🧠 RAM Usage: <code>{}%</code>
├⚡ CPU Usage: <code>{}%</code>
└🔧 Status: 🟢 Optimal</b>"""

    LOG_TEXT_G = """#NewGroup
    
👥 <b>Group Joined</b>
├📛 Name: {}
├🆔 ID: <code>{}</code>
├👥 Members: <code>{}</code>
└➕ Added By: {}"""

    LOG_TEXT_P = """#NewUser
    
👤 <b>New User</b>
├🆔 ID: <code>{}</code>
└📛 Name: {}"""
    
    NT_ADMIN_ALRT_TXT = """🚫 <b>Access Denied!</b>

You are not an admin in this group!"""

    NT_ALRT_TXT = """⚠️ Not your request!"""
    
    ALRT_TXT = """👋 Hello {},

This is not your movie request!
Please request your own content..."""

    OLD_ALRT_TXT = """👋 Hey {},

You're using an old message!
Please send a new request."""

    CUDNT_FND = SPELLING_ERROR_TXT = """⚠️ <b>No Results Found!</b>

We couldn't find what you're looking for.

🔍 <b>Suggestions:</b>
• Check your spelling
• Try different keywords
• Be more specific
• Check the suggestions below 👇</b>"""

    I_CUDNT = """<b>╔════════ ≪ °❈° ≫ ════════╗
         🔍 𝗦𝗲𝗮𝗿𝗰𝗵 𝗚𝘂𝗶𝗱𝗲 🔍
╚════════ ≪ °❈° ≫ ════════╝

📝 <b>How to Search Properly:</b>

🎥 <u>Movie Examples</u>:
┣✦ Avatar
┣✦ Avatar 2009
┣✦ The Dark Knight
┗✦ The Dark Knight 2008

📺 <u>WebSeries Examples</u>:
┣✦ Game of Thrones
┣✦ Game of Thrones S01
┣✦ Money Heist
┗✦ Money Heist S02 E05

⚠️ <b>Important:</b>
• No emojis or symbols ❌
• Use correct spelling ✅
• Include year if known 📅
• Specify season/episode</b>"""
    
    I_CUD_NT = """<b>🔍 No Results for: {}

📋 <u>Possible Reasons:</u>
• OTT/DVD not released yet
• Incorrect title spelling
• Content not in our database
• Try with release year

💡 <u>Solution:</u>
• Check spelling on Google
• Add release year
• Contact admins for help</b>"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>❌ Content Unavailable

This title is currently not in our database.

🔍 Try searching for:
• Similar movies/series
• Different keywords
• Check spelling
• Contact support</b>"""

    TOP_ALRT_MSG = """🔍 Searching in database..."""

    MELCOW_ENG = """<b>╔════════ ≪ °❈° ≫ ════════╗
      🎬 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 {} 🎭
╚════════ ≪ °❈° ≫ ════════╝

👋 Hey {}!

🔍 <b>Welcome to Filmzi Movie Downloader!</b>

🎯 <b>You can search for:</b>
• Latest Movies 🍿
• Popular WebSeries 📺
• HD Quality Content ⚡

💡 <b>Simply type any movie/series name</b>
📱 <b>Need help? Message below 👇</b></b>"""
    
    DISCLAIMER_TXT = """
<b>╔════════ ≪ °❈° ≫ ════════╗
       📜 𝗗𝗶𝘀𝗰𝗹𝗮𝗶𝗺𝗲𝗿 📜
╚════════ ≪ °❈° ≫ ════════╝

🔒 <b>Legal Notice:</b>

This is an open-source project. All files are freely available on the internet or posted by others.

📋 <b>Important:</b>
• We respect copyright laws
• Content indexed from Telegram
• For educational purposes
• Contact for removal requests
• No commercial use intended

⚠️ <b>Warning:</b>
Downloading copyrighted content may violate laws in your country. Use at your own risk.</b>"""

# ... (rest of the code remains similar with enhanced UI formatting)
