from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from app.extensions import db
from config import Config
from flask_cors import CORS
from whitenoise import WhiteNoise
import os

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)

swaggerui_blueprint = get_swaggerui_blueprint(
    app.config['SWAGGER_URL'],
    app.config['API_URL'],
    config={'app_name': "ZDAI Middleware API"}
)

# Initialize Flask extensions here
db.init_app(app)
# migrate = Migrate(app, db)

# Register blueprints here
from app.main import bp as main_bp

app.register_blueprint(main_bp)

from app.chats import bp as chat_bp

app.register_blueprint(chat_bp)

from app.messages import bp as message_bp

app.register_blueprint(message_bp)

from app.models.users import Users

# Create database tables
with app.app_context():
    db.create_all()

app.register_blueprint(swaggerui_blueprint)

# add whitenoise
app.wsgi_app = WhiteNoise(app.wsgi_app, root="app/static/")


@app.route('/test/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'

# Serve Vue.js static files from the 'dist' directory
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue(path):
    print("PATH VAL", path)
    print("HAHA Serve VUE CALLED")
    if path != '' and os.path.exists("dist/" + path):
        if path.endswith(".js"):
            return send_from_directory('../dist', path, mimetype="application/javascript")
        elif path.endswith(".css"):
            return send_from_directory('../dist', path, mimetype="text/css")
        return send_from_directory('../dist', path)
        # return "PATH not exist"
    else:
        print("ELSE PARTH CALLED")
        return send_from_directory('../dist', 'index.html')
        # return "PATH exist but cant load index"


@app.route('/api')  # Your Flask API routes
def api_route():
    # Your API logic here
    return "API response"


# Catch-all route to serve the Vue.js app for all other routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("HAHA CATCH ALL CALLED")
    return send_from_directory('dist', 'index.html')


def create_app():
    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
