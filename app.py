from flask import redirect

from zdai_app import create_app
app = create_app()

from routes import chat, message, oauth2

app.register_blueprint(chat.chat_bp)
app.register_blueprint(message.message_bp)
app.register_blueprint(oauth2.oauth_ai_ad_copy_bp)


    
@app.route('/', methods=['GET'])
def index():
    return redirect(app.config['SWAGGER_URL'])

# db = app.db
# if __name__ == '__main__':
#     print("hehe")
#     app.run(debug=True)