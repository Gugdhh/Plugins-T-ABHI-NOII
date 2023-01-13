# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from HellConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 20256702  # 666666 is a placeholder. Fill your 6 digit api id
    API_HASH = ""  # replace this with your api hash
    BOT_TOKEN = "5874935627:AAGgv0c8Ad_vp-gd3EKSplDyKcl3AnoOeqE"  # Create a bot from @BotFather and paste the token here
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of hellbot else leave it as it is.
    DATABASE_URL = "postgres://lzsdumzs:hVxl2M4cZyLocKG4CUSGtuUqED44MZRw@tiny.db.elephantsql.com/lzsdumzs"  # A postgresql database url from elephantsql
    HELLBOT_SESSION = "==hEll1AZWarzUBu5tVhYeOQIiSd_R8bcYz1V2hxvR2oieEe4KOYr6nw2d0tbmhTgf7GoNclWlHUNEQ3qHyE8bnDIHZR58g76O5iGlUQwwHgPYnA7LMi9cu-8aU8-YjibhaOpMX_Ej-k4n7E5vE2VtUElhAfip37bQATz5GFA2KhT-ZQzKjVBB6R6uDOhVmsBalONBjFM07vQLuoyZl12YmHXWI75gBM4Z6evyekfLqk8gYgJ3yEZkdyIMyg-MRn5ohOVbYDKIYkLP0G8uScn3Jr4id8sIDqXXtBjg4-Up3PXSeYTGUZp53wGQQB8odqUosHfNA5vNyEY35wz_-AoZkStAZr1kH36yxqp0=bOT=="  # telethon or pyrogram string according to BOT_LIBRARY
    HANDLER = "."  # Custom Command Handler
    SUDO_HANDLER = "!"  # Custom Command Handler for sudo users.


# end of required config
# hellbot
