import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, bot
from telegram.ext import *
import time
from loadconfig import *

imagesend = 'door.jpg'
token = telebotid
bot = telegram.Bot(token)
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def msg(text):
     bot.send_message(telechatid, text)

def unknown(text):
    bot.send_photo(telechatid, open(imagesend,'rb'))
    bot.send_message(telechatid, text)


#dispatcher.add_handler(CommandHandler('Yes', test_function))

#def addFace():
#    menu_keyboard = [['/Yes'], ['/No']]
#    menu_markup = telegram.ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
#    bot.send_message(chat_id=telechatid, text='Would you like to add this face?', reply_markup=menu_markup)

#addFace()

#def test():

#     keyboard = [[InlineKeyboardButton("Yes", url='t.me/'), InlineKeyboardButton("No", callback_data='No')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     bot.send_message(telechatid, 'BLAH BLAH', reply_markup=reply_markup)


#updater.start_polling()
