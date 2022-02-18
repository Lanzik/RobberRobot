from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import time, requests, logging, telegram
from bs4 import BeautifulSoup


logging.basicConfig(
    format='salam log: %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def get_text(text, type):
    good_text = text.split("?server=", 1)[1]
    server = good_text.split("&port=", 1)[0]
    if(type == 1):
        return server
    good_text = good_text.split("&port=", 1)[1]
    port = good_text.split("&secret=", 1)[0]
    if(type == 2):
        return port
    secret = good_text.split("&secret=", 1)[1]
    return secret
def write(update: Update, context: CallbackContext):

    while(True):
        page = requests.get("https://t.me/s/ProxyMTProto")
        soup = BeautifulSoup(page.text, "html.parser")
        last_link = ''
        b = soup.find_all(class_ = "tgme_widget_message_inline_button url_button")
        if(len(b) > 0):
            break
   # print(b)
    print("what? " + str(len(b)))
    last_link = b[len(b) - 1].get('href')

    
    for item in b:
        #context.bot.send_message(chat_id = -1001674856729, text = item.get('href') + " sign")
        server = get_text(item.get('href'), 1)
        port = get_text(item.get('href'), 2)
        secret = get_text(item.get('href'), 3)
        keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Connect", url = item.get('href')))
        context.bot.send_message(chat_id = -1001498598531, text = "<b>Server:</b> <code>" + server + "</code>\n<b>Port:</b> <code>" + port 
        + "</code>\n<b>Secret:</b> <code>" + secret + "</code>\n\n @ProxyTopia", reply_markup=keyboard, parse_mode=telegram.ParseMode.HTML)
        time.sleep(20)
    last_link = b[len(b) - 1].get('href')
    while(True):
        while(True):
            page2 = requests.get("https://t.me/s/ProxyMTProto")
            soup2 = BeautifulSoup(page2.text, "html.parser")
            b = soup2.find_all(class_ = "tgme_widget_message_inline_button url_button")
            if(len(b) > 0):
                break
        item = -1
        print("last link: " + last_link)
        print("new soup: " + b[item].get('href'))
        while(True):
            if(b[item].get('href') != last_link):
               # context.bot.send_message(chat_id = -1001674856729, text = b[item].get('href') + " sign2")
                server = get_text(b[item].get('href'), 1)
                port = get_text(b[item].get('href'), 2)
                secret = get_text(b[item].get('href'), 3)
                keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Connect", url = b[item].get('href')))
                context.bot.send_message(chat_id = -1001498598531, text = "<b>Server:</b> <code>" + server + "</code>\n<b>Port:</b> <code>" + port 
                + "</code>\n<b>Secret:</b> <code>" + secret + "</code>\n\n @ProxyTopia", reply_markup=keyboard, parse_mode=telegram.ParseMode.HTML)
                time_all = soup2.find_all(class_ = "tgme_widget_message_meta")
                if((time_all[item].text).split()[0] == 'edited'):
                    last_link = b[len(b) - 1].get('href')
                    break
                item -= 1
                time.sleep(20)
                continue
            last_link = b[len(b) - 1].get('href')
            break
        time.sleep(40)
    
def stop(update: Update, context: CallbackContext):
    update.s
def main() -> None:
    updater = Updater(token = "TOKEN", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("write", write))
    dispatcher.add_handler(CommandHandler("stop", stop))
    updater.start_polling()
    #updater.stop
    updater.idle()

if __name__ == '__main__':

    main()


    #problem!!!!!
#     Traceback (most recent call last):
#   File "/home/xlzaxsca/virtualenv/RobberRobotV1/3.9/lib/python3.9/site-packages/telegram/ext/dispatcher.py", line 555, in process_update
#     handler.handle_update(update, self, check, context)
#   File "/home/xlzaxsca/virtualenv/RobberRobotV1/3.9/lib/python3.9/site-packages/telegram/ext/handler.py", line 198, in handle_update
#     return self.callback(update, context)
#   File "/home/xlzaxsca/RobberRobotV1/public/telegram2.py", line 49, in write
#     if(b[item].get('href') != last_link):
# IndexError: list index out of range
#nabayad payame akhar ro edit kone!!!
#in bugeshe
#age dota link ya bishtar to post akhar edit beshe faghat link akhar post mishe(ino badan okesh kon)