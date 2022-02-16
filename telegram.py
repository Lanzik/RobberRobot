import time, requests, logging
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='salam log: %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def create_post(link):
    ii = 2
def check(context: CallbackContext):
    next_v_remove_duplicate = False

def write(update: Update, context: CallbackContext):
    print("inja")
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
    is_it_proxy = True
    if(is_it_proxy):
        create_post(last_link)
    
    for item in b:
        context.bot.send_message(chat_id = -1001674856739, text = item.get('href') + " emza")
        time.sleep(10)
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
                context.bot.send_message(chat_id = -1001674856739, text = b[item].get('href') + " emza2")
                time_all = soup2.find_all(class_ = "tgme_widget_message_meta")
                if((time_all[item].text).split()[0] == 'edited'):
                    last_link = b[len(b) - 1].get('href')
                    break
                item -= 1
                time.sleep(10)
                continue
            last_link = b[len(b) - 1].get('href')
            break
        time.sleep(20)
    
def stop(update: Update, context: CallbackContext):
    update.s
def main() -> None:
    updater = Updater(token = "5198112327:AAF_iHRawyU8aY58bvaq14ni8QB55Yf-fmU", use_context=True)
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