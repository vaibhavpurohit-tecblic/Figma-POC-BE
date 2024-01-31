import os

from flask import Flask, request, jsonify
from flask_cors import CORS

# from flask_swagger_ui import get_swaggerui_blueprint
from app.extensions import db
from app.generate_json import generate_json
from app.model.static_html import static_html_data
from app.model.testing import generate_html

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})


@app.route('/')
def index():
    return "server is running."


@app.route('/dynamic_html', methods=["GET"])
def static_html():
    return static_html_data


@app.route('/gen_html', methods=["POST"])
def gen_html():
    if request.method == "POST":
        json_data = request.get_json(force=True)
        # url = json_data['figma_url']
        url = "https://www.figma.com/file/3SwOZge1lyBUr2nUZtfGkf/Apricus8?type=design&node-id=68-1225&mode=design&t=xFCZAZO48CJ8Kdq1-0"
        print('Figma url :', url)

        json_file, _ = generate_json(url)
        print('json file at:', json_file)
        html_content = generate_html(json_file)

        return html_content
        response = {
            "status": 200,
            "message": "Success",
            "data": str(html_content)
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
