from flask import Flask, send_from_directory, request, jsonify
# from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate
from app.extensions import db
from app.model.testing import generate_html
from config import Config
from app.generate_json import generate_json

import os

app = Flask(__name__)


@app.route('/')
def index():
    return "server is running."

@app.route('/gen_html', methods=["POST"])
def gen_html():
    if request.method == "POST":
        json_data = request.get_json(force=True)
        url = json_data['figma_url']
        print('Figma url :',url)

        json_file, _= generate_json(url)
        print('json file at:', json_file)
        html_content = generate_html(json_file)

        response = {
            "status": 200,
            "message": "Success",
            "data" : str(html_content)
        }

        return jsonify(response)
    else:
        response = {
            "status": 405,
            "message": "Method Not Allowed"
        }

        return jsonify(response)


def create_app():
    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
