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

    # ADDING THE MISSING CAPTION ATTRIBUTE
    CAPTION = """<b><a href="https://t.me/your_channel_link">{file_name}</a></b>\n\n<b>⚡ Uploaded by : <a href="https://t.me/your_bot_link">Filmzi Movie Downloader 🎬</a></b>"""

    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 ʜᴇʏ {},</b>

<blockquote>💖 <b>ᴘʟᴇᴀꜱᴇ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ</b></blockquote>

<b>🔧 ᴛᴏ ᴋᴇᴇᴘ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ᴀʟɪᴠᴇ, ᴀᴅᴅ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇꜱ & ᴜᴘʟᴏᴀᴅ ʙᴇꜱᴛ ᴍᴏᴠɪᴇꜱ/ᴡᴇʙꜱᴇʀɪᴇꜱ ɴᴏɴ-ꜱᴛᴏᴘ ɪɴ ʜɪɢʜ Qᴜᴀʟɪᴛʏ, ᴡᴇ ɴᴇᴇᴅ ʏᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ.
ɪᴛ ʜᴇʟᴘꜱ ᴜꜱ ᴘᴀʏ ꜰᴏʀ ʜᴇʀᴏᴋᴜ & ꜱᴇʀᴠᴇʀ ʀᴇꜱᴏᴜʀᴄᴇꜱ.</b>

<b>🌝 ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ʜᴀᴠᴇ.</b>

<blockquote>🎉 <b>ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇᴛʜᴏᴅ 👇</b></blockquote>

➤ 📷 Qʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  
➤ 💸 ᴜᴘɪ ɪᴅ → <code>{}</code>

‼️ <b>ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴅᴏɴᴀᴛɪɴɢ.</b>"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""

    MOVIE_UPDATE_NOTIFY_TXT = """
</b><a href={poster_url}>📥 </a><a href={imdb_url}>NEW {tag} ADDED</a></b>

✨ ᴛɪᴛʟᴇ : <code>{filename}</code>
─┉─•✦•─┉─
<blockquote>🎭 ɢᴇɴʀᴇs : <b>{genres}</b>
🍿 ᴏᴛᴛ        : <b>{ott}</b>
🎬 ǫᴜᴀʟɪᴛʏ : <b>{quality}</b>
🔉 ᴀᴜᴅɪᴏ    : <b>{language}</b>
🌟 ʀᴀᴛɪɴɢ   : <b>{rating}</b>
{episodes} </blockquote>
─┉─•✦•─┉─

🔍 <b>Sᴇᴀʀᴄʜ →</b> {search_link}
"""
    
    IMDB_TEMPLATE_TXT = """
<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings> ({rating}</a> /10 )


⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
Requested by : {message.from_user.mention}</b>"""

    LOGO = """
╭━━━┳━━━┳━━━┳━━━┳━╮╭━┳━━━┳━━┳━╮╱╭┳━━━┳━━━━┳━━━┳━╮╱╭┳━━━╮
┃   [FILMZI MOVIE DOWNLOADER WORKING PROPERLY]   ┃
╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━┻━━┻╯╰╯╰┻━━━┻━━━━┻━━━┻╯╰╯╰┻━━━╯
"""

    # PLANS
    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<blockquote>🎖️ <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</b></blockquote>

◉ 07 ᴅᴀʏꜱ - 10 ₹  / 10 ꜱᴛᴀʀ
◉ 15 ᴅᴀʏꜱ - 20 ₹  / 20 ꜱᴛᴀʀ
◉ 30 ᴅᴀʏꜱ - 40 ₹  / 40 ꜱᴛᴀʀ
◉ 45 ᴅᴀʏꜱ - 55 ₹  / 55 ꜱᴛᴀʀ
◉ 60 ᴅᴀʏꜱ - 75 ₹  / 75 ꜱᴛᴀʀ

•─────•─────────•─────•
🏷️ <a href='https://t.me/your_channel'>ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""

    PREMIUM_STAR_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ ⭐</blockquote>

ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ᴜꜱɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ.  

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ᴛᴀᴋᴇ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ - @your_support_group

ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴘᴜʀᴄʜᴀꜱᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 👇.</b>
"""

    PREMIUM_UPI_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴜᴘɪ</blockquote>

ʏᴏᴜ ᴄᴀɴ ᴘᴜʀᴄʜᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ , ɴᴇᴛ ʙᴀɴᴋɪɴɢ.

💳 ᴜᴘɪ ɪᴅ - <code>{}</code>

💢 ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴘʟᴇᴀꜱᴇ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.</b>"""
    
    BPREMIUM_TXT = """<blockquote>🎁 <b>ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ</b> :</blockquote>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
○ ᴀᴅ-ꜰʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-ꜱᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋꜱ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

• ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ ʙʏ ʀᴇꜰᴇʀɪɴɢ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴏʀ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ 

•─────•─────────•─────•
◉ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ : /myplan

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""  

    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎖️ <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴꜱ</b></blockquote>

◉ 07 ᴅᴀʏꜱ - 10 ₹  
◉ 15 ᴅᴀʏꜱ - 20 ₹  
◉ 30 ᴅᴀʏꜱ - 40 ₹  
◉ 45 ᴅᴀʏꜱ - 55 ₹  
◉ 60 ᴅᴀʏꜱ - 75 ₹  

•─────•─────────•─────•

🏷️ <b>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅꜱ</b>

💸 ᴜᴘɪ ɪᴅ → <code>{}</code>  
📷 ǫʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  

🧾 ᴘᴀʏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ!

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.  
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ, ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.

💎 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ → /myplan</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ <a href='https://t.me/your_bot'>Owner</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>{}</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    SOURCE_TXT ="""<b>ՏOᑌᖇᑕᗴ ᑕOᗪᗴ : 👇 </b>

This Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited.\n
ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› : <a href=https://github.com/your_repo/filmzi-movie-downloader.git>ꜰɪʟᴍᴢɪ ᴍᴏᴠɪᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ</a>\n """

    SETTING_TXT = """    
<u>ꜱᴇᴛᴛɪɴɢꜱ</u> :
- ꜱᴇᴛᴛɪɴɢꜱ ɪꜱ ᴛʜᴇ ᴍᴏꜱᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ꜰᴇᴀᴛᴜʀᴇ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ.
- ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜɪꜱ ʙᴏᴛ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</u> :
• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""
    
    VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""
    

    VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<b><i>👋 ʜᴇʏ {},
    
📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</i></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3ʀᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</i></b>"""

    VERIFIED_LOG_TEXT = """ᴜꜱᴇʀ ᴠᴇʀɪꜰɪᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓

👤 ɴᴀᴍᴇ:- {} [ <code>{}</code> ]

📆 ᴅᴀᴛᴇ:- <code>{} </code>

#Verificaton_{}_Completed"""


    ADMIN_CMD = """ʜᴇʏ 👋,

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊

• /start - <code>ᴛᴏ ᴜꜱᴇ ᴍʏ ꜰᴇᴀᴛᴜʀᴇꜱ.</code>
• /stats - <code>ɢᴇᴛ ᴛʜᴇ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ ᴀɴᴅ ᴄʜᴀᴛꜱ.</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...</code>
• /movie_update - <code>ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code> 
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /verify - <code>ᴛᴜʀɴ ᴏɴ / ᴏꜰꜰ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    GROUP_CMD = """ʜᴇʏ 👋,
📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ɢʀᴏᴜᴘꜱ ⇊

• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""
