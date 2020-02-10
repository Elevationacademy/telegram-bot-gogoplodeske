from flask import Flask, Response, request
import requests

def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return False


app = Flask(__name__)
TOKEN = '957382895:AAEa9fmcuAZfWAoVKtzSGvRQIDVlbjIeEAg'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://45b344ef.ngrok.io/message'.format(TOKEN)
#requests.get(TELEGRAM_INIT_WEBHOOK_URL)



@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    chat_id = request.get_json()['message']['chat']['id']
   # res2 = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
    #                    .format(TOKEN, chat_id, "got it"))
    print(request.get_json()['message']['text'])
    txt = request.get_json()['message']['text']

    num =txt.strip('\\')
    print(num)
    num = num.strip('check')
    print(num)
    num1 = int(num)
    print(num1)
    if is_prime(num1):
        res3 = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                           .format(TOKEN, chat_id, "prime"))
    else:
        res4 = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                               .format(TOKEN, chat_id, "not prime"))

    return Response("success")

if __name__ == '__main__':
    app.run(port=5002)
