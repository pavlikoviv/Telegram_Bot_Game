import requests
import datetime
import Game_class

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=100):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        print("offset", offset)
        print("result_json",result_json)
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        print('text',text)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        print('get_result', get_result)

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        print("last_update ",last_update)
        return last_update


# def get_updates_json(request):
#     params = {'timeout': 10, 'offset': None}
#     response = requests.get(request + 'getUpdates', data=params)
#     return response.json()


token = "1187548883:AAFas-UmzsOO7svXf5EOwsNjVvDF7sCSnb4"
greet_bot = BotHandler(token)
greetings = Game_class.verb_dict
now = datetime.datetime.now()

def main():
    new_offset = None
    #today = now.day
    hour = now.hour

    while True:
        print("hour ",hour)
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        print("last_chat_text",last_chat_text)
        last_chat_id = last_update['message']['chat']['id']
        print('last_chat_id ',last_chat_id)
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and 6 <= hour < 12:
            Game_class.main()
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            #today += 1

        new_offset = last_update_id + 1
        print(new_offset)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
