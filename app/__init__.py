from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate
from app.extensions import db
from config import Config

app = Flask(__name__)
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


@app.route('/test/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'


def create_app():
    return app
