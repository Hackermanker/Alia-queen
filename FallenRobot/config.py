import json
import os


def get_user_list(config, key):
    with open("{}/FallenRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 11547196  # integer value, dont use ""
    API_HASH = "374c113817cc85b86a752c24871c7f30"
    TOKEN = "5460012894:AAFxdtKBQnDu71ODYNuLovN_DUX_uOGgoGU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1720798016  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Oriksonic"
    SUPPORT_CHAT = "botsupportastra"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001586925131
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001586925131
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://jpxynglg:m-AB1UB3OKtEeAwtFCQq3BwSX20vJcc8@tyke.db.elephantsql.com/jpxynglg"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "0RzO543wM9WrSAf3TjLfUfsyB2OufdNZirk~LX3mESrDUN9HwulJcJG_AS0iRV0Z"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 5583671735
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 5583671735
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 5384058467
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = 5384058467
    DONATION_LINK = "https://t.me/Oriksonic"  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "XGYVC1ANLYSKVK37"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
