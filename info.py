import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
API_ID       = int(os.environ.get("API_ID", ""))
API_HASH     = os.environ.get("API_HASH", "")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "")
SESSION      = os.environ.get("SESSION", "Yato")
DATABASE_URI = os.environ.get("DATABASE_URI", "")
LOG_CHANNEL  = int(os.environ.get("LOG_CHANNEL", "-1001868871195"))
ADMIN        = int(os.environ.get("ADMIN", "6497757690"))
CHANNEL      = os.environ.get("CHANNEL", "codeflix_bots")

#--------------------------------------------
