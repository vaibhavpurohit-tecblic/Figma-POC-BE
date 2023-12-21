import os
import logging
from flask import redirect, session, jsonify, request, Blueprint, url_for
from app.main import bp
from authlib.integrations.flask_client import OAuth
import requests
import json
from app.extensions import db
from app import app
from config import Config
from app.utils import register_new_user, store_access_token_in_database, retrieve_access_token_from_database, update_chat_title

logging.basicConfig(level=logging.DEBUG)
app.secret_key = 'maverick!@#$%secret'  # Replace with a secret key

oauth = OAuth(app)


@bp.route('/docs', methods=['GET'])
def index():
    return redirect(app.config['SWAGGER_URL'])


# Define the OAuth provider configuration
oauth.register(
    name='zendrop',
    client_id='2',  # Client ID
    client_secret='H7HLcuvmsmBxv4Z72YLLmrUnorZgq59AcuKqr56N',  # Client Secret
    authorize_url='https://account.staging.zendrop.com/oauth-server/authorize',
    authorize_params=None,
    authorize_params_callback=None,
    access_token_url='https://account.staging.zendrop.com/oauth-server/token',
    access_token_params=None,
    access_token_params_callback=None,
    refresh_token_url='https://account.staging.zendrop.com/oauth-server/token/refresh',
    redirect_uri='https://zdai-ad-copy-745906f359ba.herokuapp.com/authorize',
    client_kwargs={'scope': 'read-user zendrop-ai'}
)


# Define the route for handling OAuth authorization
@bp.route('/login', methods=['GET'])
def login():
    # return oauth.zendrop.authorize_redirect(redirect_uri=url_for('main.authorize', _external=True))
    return oauth.zendrop.authorize_redirect()


# Define the callback route for handling the OAuth response
@bp.route('/authorize', methods=["GET"])
def authorize():
    token = oauth.zendrop.authorize_access_token()
    session['oauth_token'] = token

    Config.API_ENDPOINT_ACCESS_TOKEN = token['access_token']
    os.environ["API_ENDPOINT_ACCESS_TOKEN"] = token['access_token']
    print("Authorization Successful")
    print(f"Config.API_ENDPOINT_ACCESS_TOKEN: {Config.API_ENDPOINT_ACCESS_TOKEN}")
    print(f"ENV ++++ API_ENDPOINT_ACCESS_TOKEN: {os.environ['API_ENDPOINT_ACCESS_TOKEN']}")

    response = redirect('/')
    # response.set_cookie('access_token', Config.API_ENDPOINT_ACCESS_TOKEN)
    response.set_cookie('is_login', "True")

    try:
        user_details = json.loads(fetch_user_details().data.decode('utf-8'))['data']['user']
        register_new_user(user_details, db)

        # Store the token in the database associated with the user
        store_access_token_in_database(user_details["id"], token['access_token'])
    except Exception as e:
        logging.error(f"ERROR :: Authorization endpoint is failing :: {e}")

        return {
            "status": 401,
            "message": "Unauthorized to enter OAUTH"
        }

    response.set_cookie('userID', str(user_details["id"]))
    response.set_cookie('userName', user_details["name"])

    return response


# Define a logout route
@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('oauth_token', None)
    # Config.API_ENDPOINT_ACCESS_TOKEN = None
    print("Logout Successful")

    response = redirect('/')
    # response.set_cookie('access_token', Config.API_ENDPOINT_ACCESS_TOKEN)
    response.delete_cookie('is_login')

    return response


@bp.route('/api/user_details', methods=["GET"])
def fetch_user_details():
    if request.method == "GET":
        # API endpoint to fetch user details
        endpoint = 'https://app.staging.zendrop.com/api/oauth-user'

        #
        # user_id = int(request.cookies.get('userID'))
        #
        # # Retrieve the token from the database using the user ID
        # bearer_token = retrieve_access_token_from_database(user_id)
        #
        # print("I am bearer value", bearer_token)
        #
        # if bearer_token is None:
        #     return jsonify({"error": "Bearer token not set. Please authenticate first."})
        #
        # # Set up the headers with the Bearer token
        # headers = {'Authorization': f"Bearer {bearer_token}"}
        headers = {'Authorization': f"Bearer {Config.API_ENDPOINT_ACCESS_TOKEN}"}

        try:
            # Make the HTTP GET request
            endpoint_response = requests.get(endpoint, headers=headers)
            user_data = endpoint_response.json()
            response = {
                "status": 200,
                "data": {
                    "user": user_data
                },
                "message": "Success"
            }

            logging.info(f"User Details fetched from Oauth")
            return jsonify(response)
        except Exception as e:
            response = {
                "status": 401,
                "message": "Unauthorized"
            }
            logging.error(f"FAILED :: User Details fetched from Oauth: {e}")
            return jsonify(response)


trending_product_stub = [
    {
        "id": 1,
        "product_name": "Zebronic Motherboard",
        "supplier": "TechZone Electronics",
        "product_cost": 89.99
    },
    {
        "id": 2,
        "product_name": "Diwali Candles",
        "supplier": "Festive Delights",
        "product_cost": 12.99
    },
    {
        "id": 3,
        "product_name": "POCO X5 Pro 5G",
        "supplier": "Gadget Haven",
        "product_cost": 299.99
    }
]


@bp.route('/api/trending_products', methods=['GET', 'POST'])
def trending_products():
    if request.method == "GET":
        response = {
            "status": 200,
            "data": {
                "trending_product": trending_product_stub
            },
            "message": "Success"
        }

        return jsonify(response)
    

@bp.route('/api/change_title', methods=["POST"])
def change_title():
    if request.method == "POST":
        chat_id = request.get_json()['chat_id']
        new_title = request.get_json()['new_title']
        
        update_chat_title(chat_id, new_title)

        response = {
            "status": 200,
            "message": "Success"
        }

        return jsonify(response)
    else:
        response = {
            "status": 405,
            "message": "Method Not Allowed"
        }

        return jsonify(response)
