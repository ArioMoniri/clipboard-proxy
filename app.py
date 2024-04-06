from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '6602337247:AAGmOgJZioTm0BGeADT8t_80EySUK0TLA_M'
TELEGRAM_CHAT_ID = '130006173'
TELEGRAM_SEND_MESSAGE_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
TELEGRAM_SEND_PHOTO_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'

@app.route('/send', methods=['POST'])
def send():
    if 'text' in request.json:
        text = request.json['text']
        requests.post(TELEGRAM_SEND_MESSAGE_URL, json={'chat_id': TELEGRAM_CHAT_ID, 'text': text})
    elif 'image' in request.files:
        image = request.files['image']
        requests.post(TELEGRAM_SEND_PHOTO_URL, data={'chat_id': TELEGRAM_CHAT_ID}, files={'photo': image})
    return "Content sent to Telegram"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
