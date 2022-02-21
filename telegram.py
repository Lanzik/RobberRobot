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

def write2(update: Update, context: CallbackContext):
    pages = {1: "https://t.me/s/ProxyMTProto", 2:"https://t.me/s/MTP_roto", 3:"https://t.me/s/TelMTProto"}
    LL_pages = {1: "", 2: "", 3: ""}
    index = 1
    while(True):
        while(True):
            page = requests.get(pages[index])
            soup = BeautifulSoup(page.text, "html.parser")
            b = soup.find_all(class_ = "tgme_widget_message_inline_button url_button")
            if(len(b) > 0):
                break
        item = -1
        print("last link" + str(index) + ": " + LL_pages[index])
        print("new soup: " + b[item].get('href'))
        while(True):
            if(b[item].get('href') != LL_pages[index]):
                server = get_text(b[item].get('href'), 1)
                port = get_text(b[item].get('href'), 2)
                secret = get_text(b[item].get('href'), 3)
                keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Connect", url = b[item].get('href')))
                context.bot.send_message(chat_id = -110014985985236, text = "<b>Server:</b> <code>" + server + "</code>\n<b>Port:</b> <code>" + port 
                + "</code>\n<b>Secret:</b> <code>" + secret + "</code>\n\n @ProxyTopia", reply_markup=keyboard, parse_mode=telegram.ParseMode.HTML)
                time_all = soup.find_all(class_ = "tgme_widget_message_meta")
                if((time_all[item].text).split()[0] == 'edited'):
                    LL_pages[index] = b[len(b) - 1].get('href')
                    break
                item -= 1
                time.sleep(20)
                if(LL_pages[index] == ""):
                    LL_pages[index] = b[len(b) - 1].get('href')
                    break
                continue
            LL_pages[index] = b[len(b) - 1].get('href')
            break
        if(index == 3):
            index = 1
        else:
            index += 1
        time.sleep(40)

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
        #context.bot.send_message(chat_id = -10101674856739, text = item.get('href') + " sign")
        server = get_text(item.get('href'), 1)
        port = get_text(item.get('href'), 2)
        secret = get_text(item.get('href'), 3)
        keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Connect", url = item.get('href')))
        context.bot.send_message(chat_id = -101014198598536, text = "<b>Server:</b> <code>" + server + "</code>\n<b>Port:</b> <code>" + port 
        + "</code>\n<b>Secret:</b> <code>" + secret + "</code>\n\n @ProxyTopia", reply_markup=keyboard, parse_mode=telegram.ParseMode.HTML)
        time.sleep(20)
    last_link = b[len(b) - 1].get('href')
    pages = {1: "https://t.me/s/ProxyMTProto", 2:"https://t.me/s/MTProxyStar", 3:"https://t.me/s/TelMTProto"}
    LL_pages = {1: last_link, 2: "", 3: ""}
    index = 1
    while(True):
        while(True):
            page2 = requests.get(pages[index])
            soup2 = BeautifulSoup(page2.text, "html.parser")
            b = soup2.find_all(class_ = "tgme_widget_message_inline_button url_button")
            if(len(b) > 0):
                break
        item = -1
        print("last link" + str(index) + ": " + LL_pages[index])
        print("new soup: " + b[item].get('href'))
        while(True):
            if(b[item].get('href') != LL_pages[index]):
               # context.bot.send_message(chat_id = -100167148561739, text = b[item].get('href') + " sign2")
                server = get_text(b[item].get('href'), 1)
                port = get_text(b[item].get('href'), 2)
                secret = get_text(b[item].get('href'), 3)
                keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Connect", url = b[item].get('href')))
                context.bot.send_message(chat_id = -10014985198536, text = "<b>Server:</b> <code>" + server + "</code>\n<b>Port:</b> <code>" + port 
                + "</code>\n<b>Secret:</b> <code>" + secret + "</code>\n\n @ProxyTopia", reply_markup=keyboard, parse_mode=telegram.ParseMode.HTML)
                time_all = soup2.find_all(class_ = "tgme_widget_message_meta")
                if((time_all[item].text).split()[0] == 'edited'):
                    LL_pages[index] = b[len(b) - 1].get('href')
                    break
                item -= 1
                LL_pages[index] = b[len(b) - 1].get('href')
                time.sleep(20)
                continue
            break
        if(index == 3):
            index = 1
        else:
            index += 1
        time.sleep(40)
    
def main() -> None:
    updater = Updater(token = "Token", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("write", write))
    dispatcher.add_handler(CommandHandler("write2", write2))
    updater.start_polling()
    #updater.stop
    updater.idle()

if __name__ == '__main__':

    main()

