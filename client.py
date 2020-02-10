import requests
s
TOKEN = '957382895:AAEa9fmcuAZfWAoVKtzSGvRQIDVlbjIeEAg'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://c374625b.ngrok.io/message'.format(TOKEN)
get =requests.get(TELEGRAM_INIT_WEBHOOK_URL)
print(get.text)
