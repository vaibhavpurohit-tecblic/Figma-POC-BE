from flask import redirect

from app import app
from routes import chat, message

app.register_blueprint(chat.chat_bp)
app.register_blueprint(message.message_bp)


@app.route('/', methods=['GET'])
def index():
    return redirect(app.config['SWAGGER_URL'])


if __name__ == "__main__":
    app.run(debug=True)
