from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '6602337247:AAGmOgJZioTm0BGeADT8t_80EySUK0TLA_M'
TELEGRAM_CHAT_ID = '130006173'
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

@app.route('/sendToTelegram', methods=['POST'])
def send_to_telegram():
    message = request.json.get('message')
    if message:
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message
        }
        response = requests.post(TELEGRAM_URL, json=payload)
        return jsonify({'status': 'success', 'response': response.text}), 200
    return jsonify({'status': 'error', 'message': 'Message is required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
