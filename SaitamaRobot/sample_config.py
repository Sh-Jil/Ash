# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1479154  # integer value, dont use ""
    API_HASH = "6b21cb22818e09132fb904705c31d3a1"
    TOKEN = "1573095785:AAEvmH6ZciLJmQuCeDLw1INZ9huLTbpEphg"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 727037917  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "shijilraj"
    SUPPORT_CHAT = 'cinemapranthanmaar'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001474921230  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001190806654  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename' # needed for any database modules
    REDIS_URI = "redis-18022.c56.east-us.azure.cloud.redislabs.com:18022"
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "U55U80fi5cbPgRlu84sGSDGb73y2OA1xjKQrOPoz3dmHMCv5J5uOYowgGydQ~2fX"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'GRQWH2DONAO56AW3'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'EC91CWSFNM7F'  # Get your API key from https://timezonedb.com/api
    WALL_API = '481903'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'af36e21c66dde6ab8d1a8a23e41bc41d35cf86152c927595830218b8bd1aa4ffdb44411c9521e54523287e5f1d72a9399444695295507f722f78fb377abf7ead'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
