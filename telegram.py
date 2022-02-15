import time, requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
def create_post(link):
    ii = 2
def check(context: CallbackContext):
    next_v_remove_duplicate = False

def write(update: Update, context: CallbackContext):
    #print("inja")
    b = soup.find_all(class_ = "tgme_widget_message_inline_button url_button")
   # print(b)
    last_link = b[-1].get('href')
    is_it_proxy = True
    if(is_it_proxy):
        create_post(last_link)
    
    for item in b:
        context.bot.send_message(chat_id = -1001674856739, text = item.get('href'))
        time.sleep(10)
    last_link = b[-1].get('href')
    while(True):
        page2 = requests.get("https://t.me/s/ProxyMTProto")
        soup2 = BeautifulSoup(page2.text, "html.parser")
        b = soup2.find_all(class_ = "tgme_widget_message_inline_button url_button")
        item = -1
        print("last link: " + last_link)
        print("new soup: " + b[-1].get('href'))
        while(True):
            if(b[item].get('href') != last_link):
                context.bot.send_message(chat_id = -1001674856739, text = b[item].get('href'))
                item -= 1
                time.sleep(10)
                continue
            break
        time.sleep(20)
    
def stop(update: Update, context: CallbackContext):
    update.s
def main() -> None:
    updater = Updater(token = "5296950371:AAFHA-9KT3yMc-g4z3hAlk2eJk-G0rqdoQM", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("write", write))
    dispatcher.add_handler(CommandHandler("stop", stop))
    updater.start_polling()
    #updater.stop
    updater.idle()

if __name__ == '__main__':
    page = requests.get("https://t.me/s/ProxyMTProto")
    soup = BeautifulSoup(page.text, "html.parser")
    last_link = ''
    main()