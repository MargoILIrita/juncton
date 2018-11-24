import requests
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters

token = '704225691:AAE3-FAZdTpmJAbnfrxWlFxoUsBawuy_bjk'
url = "https://api.telegram.org/bot"+ token +"/"



def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):
    print(data)
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    user_id = (110541740, 110541740)
    user_name = user_id[0]
    if user_id[0] == user_name:
        send_mess(user_id[1], 'You have a discount!')

__urls = []

token = '704225691:AAE3-FAZdTpmJAbnfrxWlFxoUsBawuy_bjk'


def start(bot, update):
    update.message.reply_text(
        'Hello {}! Please, send me your selfie as a document'.format(update.message.from_user.first_name))

def upload_img(bot, update):
    id = 'img/' + update.message.chat.id.__str__() + '__' + update.message.from_user.first_name.__str__()
    file_id = update.message.document.file_id
    uuuu = url + 'getFile'
    response = requests.get(uuuu,data={'file_id':file_id})
    answer = response.json()
    urr = 'https://api.telegram.org/file/bot' + token + '/' + answer['result']['file_path']
    response = requests.get(urr)
    content = response.content
    f = open(id +'.jpg','wb', 0)
    f.write(content)
    f.flush()
    f.close()
    print('all')
    update.message.reply_text("Thanks! Now go to the camera")




updater = Updater(token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

image_handler = MessageHandler(Filters.document, upload_img)
dispatcher.add_handler(image_handler)

updater.start_polling()
updater.idle()

