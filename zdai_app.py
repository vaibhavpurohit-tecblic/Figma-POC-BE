from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate

from configs.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    swaggerui_blueprint = get_swaggerui_blueprint(
        app.config['SWAGGER_URL'],
        app.config['API_URL'],
        config={'app_name': "ZDAI Middleware API"}
    )

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(swaggerui_blueprint)


    return app
# with app.app_context():
#     try:
#         db.create_all()
#     except Exception as exception:
#         print("Got the following exception when attempting db.create_all() in __init__.py: " + str(exception))
#     finally:
#         print("db.create_all() in app.py was successfull - no exceptions were raised")

