#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import telegram
import time

import requests
from bs4 import BeautifulSoup

from telegram import Update, ForceReply, bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext):

    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id = update.effective_chat.id, text="I'm a bot")
    update.message.reply_text('Hi! LANZIK')
    #bot.sendMessage("inam az in")
   # print(bot.get_me())
    context.bot.send_message(chat_id = update.effective_chat.id, text = "test")
    context.bot.get_me()
   # updates = context.bot.get_updates()
   # print(updates[0])
def update(update: Update, context: CallbackContext):
    updates = context.bot.get_updates()
    print(updates[0])

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def start2(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = -1001674856739, text = "ha ha ha")
def write(update: Update, context: CallbackContext):
      #  with open('../soup.txt', 'w') as f:
       #     f.write(soup.text)
        b = soup.find_all(class_ = "tgme_widget_message_inline_button url_button")
        #print(b[1].get('href'))
        while True:
            for item in b:
                context.bot.send_message(chat_id = -1001674856739, text = item.get('href'))
            time.sleep(10)
       # print(b[-1].text)
def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token = "5145569156:AAFzplz2kzmYTa2PRvrabkqZ0-DJO85efWg", use_context=True)
 #   bot = telegram.Bot(token='5078253708:AAFrCvftHBTxbuJQST71SnZ0pytZelpA8lQ')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


    # on different commands - answer in Telegram
    #start_handler = CommandHandler("start", start)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("start2", start2))
    dispatcher.add_handler(CommandHandler("update", update))
    dispatcher.add_handler(CommandHandler("write", write))
    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    page = requests.get("https://t.me/s/ProxyMTProto")
    soup = BeautifulSoup(page.text, "html.parser")
    #tgme_widget_message_inline_button url_button
    main()