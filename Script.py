class script(object):
    START_TXT = """
<b>🎬 Hey {}! Welcome to Filmzi! 🍿</b>

<b>🌟 Your Ultimate Movie Search Companion!</b>

<b>Here you can search for your favorite movies and web series. Just send me the</b> <b>movie name with proper</b> <b><a href='https://www.google.com/'>Google</a> spelling! 🎯</b>"""
    
    GSTART_TXT = """🎬 Welcome to Filmzi - Your Movie Search Engine!"""
    
    HELP_TXT = """<b>
    
📨 Send Movie or Series Name with Year as per Google Spelling! 👍

⚠️ Example For Movies 👇

👉 Jailer
👉 Jailer 2023

⚠️ Example For Web Series 👇

👉 Stranger Things 
👉 Stranger Things S02 E04

⚠️ Don't add emojis and symbols in movie name, use letters only! ❌
</b>"""

    ABOUT_TXT = """<b>╭────[ 🎬 Filmzi Details ]────⍟
├⍟ Bot Name : <a href=https://t.me/{}>{}</a>
├⍟ Developer : <a href={}>Owner</a> 
├⍟ Library : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
├⍟ Language : <a href='https://www.python.org/download/releases/3.0/'>Python 3</a> 
├⍟ Database : <a href='https://www.mongodb.com/'>Mongo DB</a> 
├⍟ Server : <a href='https://heroku.com/'>Heroku</a> 
├⍟ Version : v2.0 [ Stable ]
╰───────────────⍟</b>"""
    
    RESTART_TXT = """
<b>{} Bot Restarted Successfully! 🎉

📅 Date : <code>{}</code>
⏰ Time : <code>{}</code>
🌐 Timezone : <code>Asia/Kolkata</code>
🛠️ Version: <code>v2.0 [ Stable ]</code>
</b>"""

    CHANNELS = """
<b>⚡ Filmzi Groups & Channels ⚡ 

▫ All New Movies & Series
▫ Fastest Bots Available
▫ Free & Easy to Use
▫ 24x7 Services Available</b>"""

    MULTI_STATUS_TXT = """<b>╭────[ 🗃 Database 1 🗃 ]────⍟</b>
│
├⋟ All Users ⋟ <code>{}</code>
├⋟ All Groups ⋟ <code>{}</code>
├⋟ Premium Users ⋟ <code>{}</code>
├⋟ All Files ⋟ <code>{}</code>
├⋟ Used Storage ⋟ <code>{}</code>
├⋟ Free Storage ⋟ <code>{}</code>
│
<b>├────[ 🗳 Database 2 🗳 ]────⍟</b>   
│
├⋟ All Files ⋟ <code>{}</code>
├⋟ Size ⋟ <code>{}</code>
├⋟ Free ⋟ <code>{}</code>
│
<b>├────[ 🤖 Bot Details 🤖 ]────⍟</b>   
│
├⋟ Uptime ⋟ {}
├⋟ RAM ⋟ <code>{}%</code>
├⋟ CPU ⋟ <code>{}%</code>   
│
├⋟ Total Files: <code>{}</code>
│
<b>╰─────────────────────⍟</b>"""

    STATUS_TXT = """<b>╭────[ 🗃 Database 🗃 ]────⍟</b>
│
├⋟ All Users ⋟ <code>{}</code>
├⋟ All Groups ⋟ <code>{}</code>
├⋟ Premium Users ⋟ <code>{}</code>
├⋟ All Files ⋟ <code>{}</code>
├⋟ Used Storage ⋟ <code>{}</code>
├⋟ Free Storage ⋟ <code>{}</code>
│
<b>├────[ 🤖 Bot Details 🤖 ]────⍟</b>   
│
├⋟ Uptime ⋟ {}
├⋟ RAM ⋟ <code>{}%</code>
├⋟ CPU ⋟ <code>{}%</code>   
│
<b>╰─────────────────────⍟</b>"""

    LOG_TEXT_G = """#NewGroup
    
Group = {}
ID = <code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
    
ID - <code>{}</code>
Name - {}
"""
    
    NT_ADMIN_ALRT_TXT = """‼️ You are not admin in this group ‼️"""

    NT_ALRT_TXT = """Not Yours!"""
    
    ALRT_TXT = """Hello {},
This is not your movie request,
Request your own..."""

    OLD_ALRT_TXT = """Hey {},
You are using one of my old messages, 
Please send the request again."""

    CUDNT_FND = SPELLING_ERROR_TXT = """⚠️ <b>We couldn't find that!</b> Check your spelling or pick from the suggestions below 👇</b>"""

    I_CUDNT = """<b>📨 Send Movie or Series Name and Year as per Google Spelling! 👍

⚠️ Example For Movies 👇

👉 Jailer
👉 Jailer 2023

⚠️ Example For Web Series 👇

👉 Stranger Things 
👉 Stranger Things S02 E04

⚠️ Don't add emojis and symbols in movie name, use letters only! ❌</b>"""
    
    I_CUD_NT = """<b>I couldn't find any movie related to {}.

Movie not available reasons:

1) OTT or DVD not released
2) Type name with year
3) Movie is not available in the database - report to admins</b>"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>⚠️ This title is currently unavailable in our database.</b>"""
    
    TOP_ALRT_MSG = """🔍 Searching for query in our database..."""

    MELCOW_ENG = """<b>👋 Hey {},\n\n🎬 Welcome to\n🌟 {} \n\n🔍 Here you can search your favorite movies or series by just typing it's name 🔎\n\n⚠️ If you're having any problem regarding downloading or something else then message here 👇</b>"""
    
    DISCLAIMER_TXT = """
<b>This is an open source project.

All the files in this bot are freely available on the internet or posted by somebody else. Just for easy searching this bot is indexing files which are already uploaded on Telegram. We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact me so that it can be removed ASAP. It is forbidden to download, stream, reproduce, share or consume content without explicit permission from the content creator or legal copyright holder. If you believe this bot is violating your intellectual property, contact the respective channels for removal. The bot does not own any of these contents, it only index the files from Telegram. 
</b>"""

    FILMZI_DONATION = DONATE_TXT = """<b>👋 Hey {},</b>

<blockquote>💖 <b>Please donate to support Filmzi development</b></blockquote>

<b>🔧 To keep this service alive, add new features & upload best movies/web series non-stop in high quality, we need your support.
It helps us pay for hosting & server resources.</b>

<b>🌝 You can donate any amount you have.</b>

<blockquote>🎉 <b>Select your donation method 👇</b></blockquote>

➤ 📷 QR Code → <a href='{}'>Click here to scan</a>  
➤ 💸 UPI ID → <code>{}</code>

‼️ <b>Must send screenshot after donating.</b>"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
Series Request Format
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

Go to Google ➠ Type series name ➠ Copy correct name ➠ Paste in this group

Example : Loki S01E01

🚯 Don't use ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

ID : <code>{}</code>
Name : {}

Message : <b>{}</b>"""
    
    CAPTION = """<b><a href="https://t.me/filmzi_updates">{file_name}</a></b>\n\n<b>⚡ Uploaded by : <a href="https://t.me/filmzi_updates">Filmzi Movie Bot 🎬</a></b>"""

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
🌟 Rating: <a href={url}/ratings>{rating}/10</a>

⏰ Result Shown in: {remaining_seconds} seconds 🔥
Requested by: {message.from_user.mention}</b>"""

    LOGO = """
╭━━━┳━━━┳━━━┳━━━┳━╮╭━┳━━━┳━━┳━╮╱╭┳━━━┳━━━━┳━━━┳━╮╱╭┳━━━╮
┃   [🎬 FILMZI MOVIE BOT WORKING PERFECTLY]   ┃
╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━┻━━┻╯╰╯╰┻━━━┻━━━━┻━━━┻╯╰╯╰┻━━━╯
"""

    # PLANS

    PAGE_TXT = """Why are you so curious? 🤔"""

    PURCHASE_TXT = """Select your payment method."""

    PREMIUM_TEXT = """<blockquote>🎖️ <b>Available Plans</b></blockquote>

◉ 07 Days - 10 ₹
◉ 15 Days - 20 ₹
◉ 30 Days - 40 ₹
◉ 45 Days - 55 ₹
◉ 60 Days - 75 ₹

•─────•─────────•─────•

🏷️ <a href='https://t.me/filmzi_updates'>Subscription Proof</a>

‼️ Must send screenshot after payment.
‼️ After sending screenshot give us some time to add you in premium list."""

    PREMIUM_STAR_TEXT = """<b><blockquote>Payment Method: Telegram Stars ⭐</blockquote>

Now you can buy our premium service using Telegram stars.  

If you face any problem, take a screenshot and send it to @filmzi_support

Select your desired amount and purchase a subscription 👇.</b>"""

    PREMIUM_UPI_TEXT = """<b><blockquote>Payment Method: UPI</blockquote>

You can purchase premium through UPI, net banking.

💳 UPI ID - <code>{}</code>

💢 Must send screenshot after payment.

‼️ After sending screenshot please give us some time to add you in premium list.</b>"""
    
    BPREMIUM_TXT = """<blockquote>🎁 <b>Premium Features</b> :</blockquote>

○ No need to verify
○ No need to open links
○ Direct files   
○ Ad-free experience 
○ High-speed download links                         
○ Multi-player streaming links                           
○ Unlimited movies & series                                                                        
○ Full admin support                              
○ Request will be completed in 1h [ if available ]

• You can get premium by referring your friends or you can buy premium service 

•─────•─────────•─────•
◉ Check your active plan : /myplan

‼️ After sending screenshot give us some time to add you in premium list."""  

    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 Hey {},

<blockquote>🎖️ <b>Available Plans</b></blockquote>

◉ 07 Days - 10 ₹  
◉ 15 Days - 20 ₹  
◉ 30 Days - 40 ₹  
◉ 45 Days - 55 ₹  
◉ 60 Days - 75 ₹  

•─────•─────────•─────•

🏷️ <b>Payment Methods</b>

💸 UPI ID → <code>{}</code>  
📷 QR Code → <a href='{}'>Click here to scan</a>  

🧾 Pay according to your plan and enjoy premium!

‼️ Must send screenshot after payment.  
‼️ After sending a screenshot, give us some time to add you in the premium list.

💎 Check your plan → /myplan</b>"""

    FREE_TXT = """<b>👋 Hey {},
    
🎉 <u>Free Trial</u> 🎉
❗ Only for 5 minutes
 
○ No need to open links
○ Multi-player streaming links
○ Ad-free experience

👨‍💻 Contact the <a href='https://t.me/Zeroboy216'>Owner</a> to get your trial.

➛ Use /plan to see all our plans at once.
➛ Check your active plan by using : /myplan</b>"""

    UPI_TXT = """<b>👋 Hey {},
    
 Pay amount according to your plan and enjoy premium membership!

💵 UPI ID - <code>{}</code>

‼️ Must send screenshot after payment.</b>"""

    QR_TXT = """<b>👋 Hey {},
    
 Pay amount according to your plan and enjoy premium membership!

📸 QR Code - <a href='{}'>Click here to scan</a>

‼️ Must send screenshot after payment.</b>"""

    SOURCE_TXT ="""<b>Source Code : 👇 </b>

This Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited.\n
Source Code Here ◉› : <a href=https://github.com/Rpedit/HD-Pro-Search-Bot.git>Filmzi Bot</a>\n """

    SETTING_TXT = """    
<u>Settings</u> :
- Settings is the most important feature of this bot.
- You can easily customize this bot for your group.

<u>Available Commands</u> :
• /settings - Change the group settings as your wish.
• /set_shortner - Set your 1st shortener.
• /set_shortner_2 - Set your 2nd shortener.
• /set_shortner_3 - Set your 3rd shortener.
• /set_tutorial - Set your 1st tutorial video.
• /set_tutorial_2 - Set your 2nd tutorial video.
• /set_tutorial_3 - Set your 3rd tutorial video.
• /set_time - Set 1st verification gap.
• /set_time_2 - Set 2nd verification gap.
• /set_log_channel - Set verification log channel.
• /set_fsub - Set custom force sub channel.
• /remove_fsub - Remove custom force sub channel.
• /reset_group - Reset your settings.
• /details - Check your settings."""
    
    VERIFICATION_TEXT = """<b><i>👋 Hey {},

📌 You are not verified today, please click on verify & get unlimited access for till next verification.

#Verification: 1/3 ✓

If you want direct files then you can take premium service (no need to verify).</i></b>"""

    VERIFY_COMPLETE_TEXT = """<b><i>👋 Hey {},

You have completed the 1st verification ✓

Now you have unlimited access for next verification.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<b><i>👋 Hey {},

📌 You are not verified, tap on the verify link and get unlimited access for till next verification.

#Verification: 2/3 ✓

If you want direct files then you can take premium service (no need to verify).</i></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 Hey {},
    
You have completed the 2nd verification ✓

Now you have unlimited access for next verification.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<b><i>👋 Hey {},
    
📌 You are not verified, tap on the verify link & get unlimited access for next full day.

#Verification: 3/3 ✓

If you want direct files then you can take premium service (no need to verify)</i></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 Hey {},
    
You have completed the 3rd verification ✓

Now you have unlimited access for next full day.</i></b>"""

    VERIFIED_LOG_TEXT = """User verified successfully ✓

👤 Name: {} [ <code>{}</code> ]

📆 Date: <code>{}</code>

#Verification_{}_Completed"""

    ADMIN_CMD = """🎬 Hey Admin!

📚 Here are my commands list for all bot admins ⇊

• /start - <code>To use my features.</code>
• /stats - <code>Get the total users and chats.</code>
• /del_msg - <code>Remove file name collection notification...</code>
• /movie_update - <code>On/Off according to your needed...</code> 
• /pm_search - <code>PM search On/Off according to your needed...</code>
• /verify - <code>Turn On/Off verification (only work in group)</code>
• /logs - <code>Get the recent errors.</code>
• /delete - <code>Delete a specific file from db.</code>
• /users - <code>Get list of my users and ids.</code>
• /chats - <code>Get list of my chats and ids.</code>
• /leave  - <code>Leave from a chat.</code>
• /disable  -  <code>Disable a chat.</code>
• /ban  - <code>Ban a user.</code>
• /unban  - <code>Unban a user.</code>
• /channel - <code>Get list of total connected groups.</code>
• /broadcast - <code>Broadcast a message to all users.</code>
• /grp_broadcast - <code>Broadcast a message to all connected groups.</code>
• /delg - <code>Delete a specific global filter.</code>
• /delallg - <code>Delete all global filters from the bot's database.</code>
• /deletefiles - <code>Delete CamRip and PreDVD files from the bot's database.</code>
• /send - <code>Send message to a particular user.</code>
• /add_premium - <code>Add any user to premium.</code>
• /remove_premium - <code>Remove any user from premium.</code>
• /premium_users - <code>Get list of premium users.</code>
• /get_premium - <code>Get info of any premium user.</code>
• /restart - <code>Restart the bot.</code>"""

    GROUP_CMD = """🎬 Hey!
📚 Here are my commands list for customized groups ⇊

• /settings - Change the group settings as your wish.
• /set_shortner - Set your 1st shortener.
• /set_shortner_2 - Set your 2nd shortener.
• /set_shortner_3 - Set your 3rd shortener.
• /set_tutorial - Set your 1st tutorial video.
• /set_tutorial_2 - Set your 2nd tutorial video.
• /set_tutorial_3 - Set your 3rd tutorial video.
• /set_time - Set 1st verification gap.
• /set_time_2 - Set 2nd verification gap.
• /set_log_channel - Set verification log channel.
• /set_fsub - Set custom force sub channel.
• /remove_fsub - Remove custom force sub channel.
• /reset_group - Reset your settings.
• /details - Check your settings."""
