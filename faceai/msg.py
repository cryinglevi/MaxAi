import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = ""
bot = telegram.Bot(token=token)


def msg(text):
    # bot.send_photo('1345754285', open(imagesend,'rb'))

     bot.send_message('1345754285', text)
