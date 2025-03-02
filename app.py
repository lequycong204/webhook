import os, sys
# sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify_webhook():
    VERIFY_TOKEN = 'hello'
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode == 'subscribe' and challenge:
        if not token == VERIFY_TOKEN:
            return 'Verification failed', 403
        return challenge
    else:
        return 'Chatbot1', 200

@app.route('/', methods=['POST'])
def receive_message():
    data = request.get_json()
    print(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                if 'message' in messaging_event:
                    message_text = messaging_event['message'].get('text')
                    print(f"Received message from {sender_id}: {message_text}")

    return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(debug=True)
