class script(object):
    START_TXT = """
<b>🎬 Welcome to Filmzi Movie Downloader!</b>

<b>👋 Hey {}! Ready for movies? 🍿</b>

<b>🔍 Search Made Easy:</b>
• Type any Movie/Series name
• Use proper Google spelling
• Get instant download links! ⚡

<b>📥 Add me to your group for unlimited access!</b>"""
    
    GSTART_TXT = """🎬 Welcome to Filmzi Movie Downloader!"""
    
    HELP_TXT = """<b>
🎯 <b>How To Use:</b>

📝 <b>Search Format:</b>

🎥 <u>Movie Examples:</u>
• Avatar
• Avatar 2009
• The Dark Knight

📺 <u>WebSeries Examples:</u>
• Game of Thrones S01
• Money Heist S02 E05

⚠️ <b>Important:</b>
• No emojis or symbols
• Correct spelling only
• Include year if known</b>"""

    ABOUT_TXT = """<b>🤖 Bot Details:

🎬 Filmzi Movie Downloader

• Bot Name: <a href=https://t.me/{}>{}</a>
• Developer: <a href={}>ZeroDev</a>
• Library: Pyrogram
• Language: Python 3
• Database: Mongo DB
• Version: v2.4 [Stable]
• Status: 🟢 Online</b>"""
    
    RESTART_TXT = """
<b>🔄 System Restarted

🤖 Bot: {}

📊 Status:
• Date: <code>{}</code>
• Time: <code>{}</code>
• Version: v1.4 [Stable]
• Status: 🟢 Operational</b>"""

    CHANNELS = """
<b>📡 Channels & Groups

🌟 Features:
• Latest Movies & Series 🎬
• Super Fast Bots ⚡
• Free & Easy to Use 🆓
• 24/7 Active Service 🌙
• HD Quality Content 🎯</b>"""

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

    I_CUDNT = """<b>🔍 Search Guide

📝 How to Search Properly:

🎥 Movie Examples:
• Avatar
• Avatar 2009
• The Dark Knight

📺 WebSeries Examples:
• Game of Thrones S01
• Money Heist S02 E05

⚠️ Important:
• No emojis or symbols ❌
• Use correct spelling ✅
• Include year if known 📅
• Specify season/episode</b>"""
    
    I_CUD_NT = """<b>🔍 No Results for: {}

📋 Possible Reasons:
• OTT/DVD not released yet
• Incorrect title spelling
• Content not in our database
• Try with release year

💡 Solution:
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

    MELCOW_ENG = """<b>🎬 Welcome to {} 🎭

👋 Hey {}!

🔍 Welcome to Filmzi Movie Downloader!

🎯 You can search for:
• Latest Movies 🍿
• Popular WebSeries 📺
• HD Quality Content ⚡

💡 Simply type any movie/series name
📱 Need help? Message below 👇</b>"""
    
    DISCLAIMER_TXT = """
<b>📜 Disclaimer

🔒 Legal Notice:

This is an open-source project. All files are freely available on the internet or posted by others.

📋 Important:
• We respect copyright laws
• Content indexed from Telegram
• For educational purposes
• Contact for removal requests
• No commercial use intended

⚠️ Warning:
Downloading copyrighted content may violate laws in your country. Use at your own risk.</b>"""

    CAPTION = """<b><a href="https://t.me/your_channel_link">{file_name}</a></b>\n\n<b>⚡ Uploaded by : <a href="https://t.me/your_bot_link">Filmzi Movie Downloader 🎬</a></b>"""

    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 Hey {},</b>

<blockquote>💖 Please donate to the developer</blockquote>

<b>🔧 To keep this service alive, add new features & upload best movies/webseries non-stop in high quality, we need your support.
It helps us pay for Heroku & server resources.</b>

<b>🌝 You can donate any amount you have.</b>

<blockquote>🎉 Select your donation method 👇</blockquote>

➤ 📷 QR code → <a href='{}'>Click here to scan</a>  
➤ 💸 UPI ID → <code>{}</code>

‼️ Must send screenshot after donating.</b>"""

    SINFO = """
Series request format

Go to Google → Type series name → Copy correct name → Paste this group

Example : Loki S01E01

Don't use → ':(!,./)"""

    NORSLTS = """ 
#NoResults

Id : <code>{}</code>
Name : {}

Message : <b>{}</b>"""

    MOVIE_UPDATE_NOTIFY_TXT = """
</b><a href={poster_url}>📥 </a><a href={imdb_url}>NEW {tag} ADDED</a></b>

✨ Title : <code>{filename}</code>
─┉─•✦•─┉─
<blockquote>🎭 Genres : <b>{genres}</b>
🍿 OTT : <b>{ott}</b>
🎬 Quality : <b>{quality}</b>
🔉 Audio : <b>{language}</b>
🌟 Rating : <b>{rating}</b>
{episodes} </blockquote>
─┉─•✦•─┉─

🔍 <b>Search →</b> {search_link}
"""
    
    IMDB_TEMPLATE_TXT = """
<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings> ({rating}</a> /10 )

⏰ Result Shown in: {remaining_seconds} seconds 🔥
Requested by : {message.from_user.mention}</b>"""

    LOGO = """
╭━━━┳━━━┳━━━┳━━━┳━╮╭━┳━━━┳━━┳━╮╱╭┳━━━┳━━━━┳━━━┳━╮╱╭┳━━━╮
┃   [FILMZI MOVIE DOWNLOADER WORKING PROPERLY]   ┃
╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━┻━━┻╯╰╯╰┻━━━┻━━━━┻━━━┻╯╰╯╰┻━━━╯
"""

    PAGE_TXT = """Why are you so curious ⁉️"""

    PURCHASE_TXT = """Select your payment method."""

    PREMIUM_TEXT = """<blockquote>🎖️ Available Plans</blockquote>

◉ 07 days - 10 ₹  / 10 star
◉ 15 days - 20 ₹  / 20 star
◉ 30 days - 40 ₹  / 40 star
◉ 45 days - 55 ₹  / 55 star
◉ 60 days - 75 ₹  / 75 star

•─────•─────────•─────•
🏷️ <a href='https://t.me/your_channel'>Subscription proof</a>

‼️ Must send screenshot after payment.
‼️ After sending screenshot give us some time to add you in premium list."""

    PREMIUM_STAR_TEXT = """<b><blockquote>Payment method: Telegram Stars ⭐</blockquote>

Now you can buy our premium service using Telegram stars.  

If you face any problem, take a screenshot and send it to - @your_support_group

Select your desired amount and purchase a subscription 👇.</b>
"""

    PREMIUM_UPI_TEXT = """<b><blockquote>Payment method: UPI</blockquote>

You can purchase premium through UPI, net banking.

💳 UPI ID - <code>{}</code>

💢 Must send screenshot after payment.

‼️ After sending screenshot please give us some time to add you in premium list.</b>"""
    
    BPREMIUM_TXT = """<blockquote>🎁 Premium Features :</blockquote>

○ No need to verify
○ No need to open links
○ Direct files   
○ Ad-free experience 
○ High-speed download link                         
○ Multi-player streaming links                           
○ Unlimited movies & series                                                                        
○ Full admin support                              
○ Request will be completed in 1h [ if available ]

• You can get premium by referring your friends or you can buy premium service 

•─────•─────────•─────•
◉ Check your active plan : /myplan

‼️ After sending screenshot give us some time to add you in premium list."""  

    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 Hey {},

<blockquote>🎖️ Available Plans</blockquote>

◉ 07 days - 10 ₹  
◉ 15 days - 20 ₹  
◉ 30 days - 40 ₹  
◉ 45 days - 55 ₹  
◉ 60 days - 75 ₹  

•─────•─────────•─────•

🏷️ Payment Methods

💸 UPI ID → <code>{}</code>  
📷 QR code → <a href='{}'>Click here to scan</a>  

🧾 Pay according to your plan and enjoy premium!

‼️ Must send screenshot after payment.  
‼️ After sending a screenshot, give us some time to add you in the premium list.

💎 Check your plan → /myplan</b>"""

    FREE_TXT = """<b>👋 Hey {},
    
🎉 Free Trial 🎉
❗ Only for 5 minutes
 
○ No need to open links
○ Multi-player streaming links
○ Ad-free experience

👨‍💻 Contact the <a href='https://t.me/your_bot'>Owner</a> to get your trial.

➛ Use /plan to see all our plans at once.
➛ Check your active plan by using : /myplan</b>"""

    UPI_TXT = """<b>👋 Hey {},
    
 Pay amount according to your plan and enjoy premium membership !

💵 UPI ID - <code>{}</code>

‼️ Must send screenshot after payment.</b>"""

    QR_TXT = """<b>👋 Hey {},
    
 Pay amount according to your plan and enjoy premium membership !

📸 QR code - <a href='{}'>Click here to scan</a>

‼️ Must send screenshot after payment.</b>"""

    SOURCE_TXT ="""<b>Source Code : 👇 </b>

This Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited.\n
Source code here ◉› : <a href=https://github.com/your_repo/filmzi-movie-downloader.git>Filmzi Movie Downloader</a>\n """

    SETTING_TXT = """    
<u>Settings</u> :
- Settings is the most important feature of this bot.
- You can easily customize this bot for your group.

<u>Available commands</u> :
• /settings - Change the group settings as your wish.
• /set_shortner - Set your 1st shortner.
• /set_shortner_2 - Set your 2nd shortner.
• /set_shortner_3 - Set your 3rd shortner.
• /set_tutorial - Set your 1st tutorial video .
• /set_tutorial_2 - Set your 2nd tutorial video .
• /set_tutorial_3 - Set your 3rd tutorial video .
• /set_time - Set 1st verification gap.
• /set_time_2 - Set 2nd verification gap.
• /set_log_channel - Set verification log channel.
• /set_fsub - Set custom force sub channel.
• /remove_fsub - Remove custom force sub channel.
• /reset_group - Reset your settings.
• /details - Check your settings."""
    
    VERIFICATION_TEXT = """<b><i>👋 Hey {},

📌 You are not verified today, please click on verify & get unlimited access for till next verification.

#Verification:- 1/3 ✓

If you want direct files then you can take premium service (no need to verify).</i></b>"""
    

    VERIFY_COMPLETE_TEXT = """<b><i>👋 Hey {},

You have completed the 1st verification ✓

Now you have unlimited access for next verification.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<b><i>👋 Hey {},

📌 You are not verified, tap on the verify link and get unlimited access for till next verification.

#Verification:- 2/3 ✓

If you want direct files then you can take premium service (no need to verify).</i></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 Hey {},
    
You have completed the 2nd verification ✓

Now you have unlimited access for next verification.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<b><i>👋 Hey {},
    
📌 You are not verified, tap on the verify link & get unlimited access for next full day.

#Verification:- 3/3 ✓

If you want direct files then you can take premium service (no need to verify)</i></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 Hey {},
    
You have completed the 3rd verification ✓

Now you have unlimited access for next full day.</i></b>"""

    VERIFIED_LOG_TEXT = """User verified successfully ✓

👤 Name:- {} [ <code>{}</code> ]

📆 Date:- <code>{} </code>

#Verificaton_{}_Completed"""

    ADMIN_CMD = """Hey 👋,

📚 Here are my commands list for all bot admins ⇊

• /start - To use my features.
• /stats - Get the total users and chats.
• /del_msg - Remove file name collection notification...
• /movie_update - On / off according to your needed...
• /pm_search - Pm search on / off according to your needed...
• /verify - Turn on / off verification (only work in group)
• /logs - Get the recent errors.
• /delete - Delete a specific file from db.
• /users - Get list of my users and ids.
• /chats - Get list of my chats and ids.
• /leave  - Leave from a chat.
• /disable  -  Disable a chat.
• /ban  - Ban a user.
• /unban  - Unban a user.
• /channel - Get list of total connected groups.
• /broadcast - Broadcast a message to all users.
• /grp_broadcast - Broadcast a message to all connected groups.
• /delg - Delete a specific global filter.
• /delallg - Delete all Gfilters from the bot's database.
• /deletefiles - Delete CamRip and PreDVD files from the bot's database.
• /send - Send message to a particular user.
• /add_premium - Add any user to premium.
• /remove_premium - Remove any user from premium.
• /premium_users - Get list of premium users.
• /get_premium - Get info of any premium user.
• /restart - Restart the bot."""

    GROUP_CMD = """Hey 👋,
📚 Here are my commands list for customized groups ⇊

• /settings - Change the group settings as your wish.
• /set_shortner - Set your 1st shortner.
• /set_shortner_2 - Set your 2nd shortner.
• /set_shortner_3 - Set your 3rd shortner.
• /set_tutorial - Set your 1st tutorial video .
• /set_tutorial_2 - Set your 2nd tutorial video .
• /set_tutorial_3 - Set your 3rd tutorial video .
• /set_time - Set 1st verification gap.
• /set_time_2 - Set 2nd verification gap.
• /set_log_channel - Set verification log channel.
• /set_fsub - Set custom force sub channel.
• /remove_fsub - Remove custom force sub channel.
• /reset_group - Reset your settings.
• /details - Check your settings."""
