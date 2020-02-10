from flask import Flask, Response, request
import requests



app = Flask(__name__)


@app.route('/sanity')
def sanity():return "Server is running"

TOKEN = '957382895:AAEa9fmcuAZfWAoVKtzSGvRQIDVlbjIeEAg'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://45b344ef.ngrok.io/message'.format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)



@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    chat_id = request.get_json()['message']['chat']['id']

    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, "Got it"))
    print( request.get_json())
    return Response("success")

if __name__ == '__main__':
    app.run(port=5002)