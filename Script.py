class script(object):
    START_TXT = """π Hai {},
πΌπ π½π°πΌπ΄ πΈπ  <a href=https://t.me/{}>{}</a>, πΈππ ππππππ π°ππππ΅πππππ π±ππ πΈ πππ πΏππππππ π°ππ ππππππ"""          
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: <a href=https://t.me/mr_MKN>Mr MKN TG</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎπ³π±
β― π±πΎπ ππ΄πππ΄π: ΰ΄ΰ΄²ΰ΅ΰ΄² π
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [πΌπ°πΉπΎπ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a EvaMaria project
- Source - https://github.com/EvamariaTG/EvaMaria 

<b>DEVS:</b>
- <a href=https://t.me/mkn_bots_updates>MKN BOTZ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. this bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /start - bot alive
β’ /settings - bot settings
β’ /stats - to get status of files in
β’ /set_template - set imdb temp db.
β’ /autofilter  - AutoFilter on/off
β’ /instatus - inline status
β’ /purge - delet chat message 
β’ /logs - to get the rescent errors
β’ /filter - add manual filters
β’ /filters - view filters
β’ /connect - connect to PM.
β’ /disconnect - disconnect from PM
β’ /del - delete a filter
β’ /delall - delete all filters
β’ /deleteall - delete all index(autofilter)
β’ /delete - delete a specific file from index.
β’ /info - get user info
β’ /id - get tg ids.
β’ /imdb - fetch info from imdb.
β’ /users - to get list of my users and ids.
β’ /chats - to get list of the my chats and ids 
β’ /index  - to add files from a channel
β’ /leave  - to leave from a chat.
β’ /disable  -  do disable a chat.
β’ /enable - re-enable chat.
β’ /ban  - to ban a user.
β’ /unban  - to unban a user.
β’ /channel - to get list of total ch
β’ /broadcast - to broadcast a message to all
β’ /batch - to create link for multiple posts
β’ /link - to create link for one post"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}

By - @MKN_thorappan_bot
"""
