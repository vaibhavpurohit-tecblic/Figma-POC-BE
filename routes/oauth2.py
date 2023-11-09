from flask import Flask, redirect, url_for, session, request, Blueprint, jsonify
from authlib.integrations.flask_client import OAuth
from app import app
import requests


oauth_ai_ad_copy_bp = Blueprint('oauth-ai-ad-copy', __name__)

app.secret_key = 'maverick!@#$%secret'  # Replace with a secret key

oauth = OAuth(app)
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
    client_kwargs={'scope': 'read-user zendrop-academy'}
)


# Define the route for handling OAuth authorization
@oauth_ai_ad_copy_bp.route('/login', methods=['GET'])
def login():
    # return oauth.zendrop.authorize_redirect(redirect_uri=url_for('oauth-ai-ad-copy.authorize', _external=True))
    return oauth.zendrop.authorize_redirect()


# Define the callback route for handling the OAuth response
@oauth_ai_ad_copy_bp.route('/authorize', methods=["GET"])
def authorize():
    token = oauth.zendrop.authorize_access_token()
    session['oauth_token'] = token

    # You can retrieve user data or make API requests here using the access token.
    print(f"Access Token: {token}")

    return 'You are now logged in.'


# Define a logout route
@oauth_ai_ad_copy_bp.route('/logout', methods=['GET'])
def logout():
    session.pop('oauth_token', None)
    return 'You are now logged out.'


if __name__ == '__main__':
    app.run()
