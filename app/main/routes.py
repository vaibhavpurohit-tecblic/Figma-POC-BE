from flask import redirect, session, jsonify, request, Blueprint, url_for
from app.main import bp
from authlib.integrations.flask_client import OAuth
import requests
from app import app
from config import Config

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
    print("Authorization Successful")

    return redirect('/')


# Define a logout route
@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('oauth_token', None)
    return 'You are now logged out.'


@bp.route('/api/user_details', methods=["GET"])
def fetch_user_details():
    if request.method == "GET":
        # API endpoint to fetch user details
        endpoint = 'https://app.staging.zendrop.com/api/oauth-user'

        # Set up the headers with the Bearer token
        headers = {'Authorization': f"Bearer {Config.API_ENDPOINT_ACCESS_TOKEN}"}

        # Make the HTTP GET request
        endpoint_response = requests.get(endpoint, headers=headers)
        user_data = endpoint_response.json()
        response = {
            "status": "ok",
            "data": {
                "user": user_data
            },
            "message": ""
        }

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
            "status": "ok",
            "data": {
                "trending_product": trending_product_stub
            },
            "message": ""
        }

        return jsonify(response)
