from time import sleep

import requests

url = "https://api.telegram.org/bot704225691:AAE3-FAZdTpmJAbnfrxWlFxoUsBawuy_bjk/"


def get_updates_json(request):
    print(request + 'getUpdates')
    response = requests.get(request + 'getUpdates')
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

if __name__ == '__main__':
    main()