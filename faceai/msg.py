#fb email token from emailondeck bdaf37b61a3e20be2bf4ca7b6f5518df

import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "1559670838:AAF2s09xvuOQ_AEiXZgYWhZmneQ5He5gSBc"
bot = telegram.Bot(token=token)

imagesend = 'obama.jpg'

def msg(text):
    # bot.send_photo('1345754285', open(imagesend,'rb'))

     bot.send_message('1345754285', text)
