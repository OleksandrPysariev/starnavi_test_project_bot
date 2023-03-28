import os
from config_parser.parser import ConfigParser
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("domain")
PORT = os.getenv("port")

ADDRESS = f"{DOMAIN}:{PORT}"
CREDENTIALS_FILENAME = "credentials.csv"

config = ConfigParser().parse(os.getenv("filename"))

NUMBER_OF_USERS = int(config.get("bot", "number_of_users"))
MAX_POSTS_PER_USER = int(config.get("bot", "max_posts_per_user"))
MAX_LIKES_PER_USER = int(config.get("bot", "max_likes_per_user"))
