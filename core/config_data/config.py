import logging
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (("start", "Start bot"),)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
