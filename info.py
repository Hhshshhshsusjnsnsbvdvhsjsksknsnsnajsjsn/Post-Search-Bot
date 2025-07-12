import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
API_ID       = int(os.environ.get("API_ID", "28264594"))
API_HASH     = os.environ.get("API_HASH", "94ca8a089020a2290fd29a41f18acb94")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6427124758:AAG-PILGXW3q-RGlgajUNbQJr6F0pWmqStQ")
SESSION      = os.environ.get("SESSION", "")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://publicdb:publicdb@cluster0.aisg0rh.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL  = int(os.environ.get("LOG_CHANNEL", "-1001868871195"))
ADMIN        = int(os.environ.get("ADMIN", "6497757690"))
CHANNEL      = os.environ.get("CHANNEL", "codeflix_bots")

#--------------------------------------------
