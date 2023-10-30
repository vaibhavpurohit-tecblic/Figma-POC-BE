from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from configs.config import Config

app = Flask(__name__)
app.config.from_object(Config)

swaggerui_blueprint = get_swaggerui_blueprint(
    app.config['SWAGGER_URL'],
    app.config['API_URL'],
    config={'app_name': "ZDAI Middleware API"}
)

db = SQLAlchemy(app)

app.register_blueprint(swaggerui_blueprint)
