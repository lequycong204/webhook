from flask import Flask, render_template, request

app = Flask(__name__)
application = app
# # Configure your Flask app and Mail settings

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.get('/')
def verify():
    #Webhook verification 
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200 
    return "Chatbot", 200
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
