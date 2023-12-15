import os

from flask import jsonify, request
from app.products import bp
import requests
from config import Config


# Define the callback route for handling the OAuth response
@bp.route('/api/products', methods=["GET"])
def import_list_products():
    print(request.host)
    print(request.host_url)
    print(request.trusted_hosts)
    if request.method == "GET":
        # API endpoint to fetch list of products.
        endpoint = 'https://app.staging.zendrop.com/api/oauth-import-list-products'
        bearer_token = Config.API_ENDPOINT_ACCESS_TOKEN or os.getenv("API_ENDPOINT_ACCESS_TOKEN")
        print(f"BEARER CONfig: {Config.API_ENDPOINT_ACCESS_TOKEN}")
        print(f"BEARER from ENV: {os.getenv('API_ENDPOINT_ACCESS_TOKEN')}")

        print("I am bearer value", bearer_token)

        if bearer_token is None:
            return jsonify({"error": "Bearer token not set. Please authenticate first."})

        # Set up the headers with the Bearer token
        headers = {'Authorization': f"Bearer {bearer_token}"}

        # Make the HTTP GET request
        endpoint_response = requests.get(endpoint, headers=headers)
        # print("ENDPOINT RESPONSE TEXT -->", endpoint_response.text)

        if endpoint_response.status_code == 200:
            try:
                products_data = endpoint_response.json()
                response = {"products_data": products_data}
                return jsonify(response)
            except requests.exceptions.JSONDecodeError as e:
                # Handle JSONDecodeError
                print(f"JSONDecodeError: {e}")
                return jsonify({"error": "Invalid JSON response"})
        else:
            # Handle non-200 status codes
            return jsonify({"error": f"API request failed with status code {endpoint_response.status_code}"})

        # products_data = endpoint_response.json()
        # response = {
        #     "products_data": products_data,
        # }
        #
        # return jsonify(response)


@bp.route('/api/products/<int:product_id>', methods=['GET'])
def import_list_product_detail(product_id):
    if request.method == "GET":
        # API endpoint to fetch list of products.
        endpoint = f'https://app.staging.zendrop.com/api/oauth-import-list-products/{product_id}'

        # Set up the headers with the Bearer token
        headers = {'Authorization': f"Bearer {Config.API_ENDPOINT_ACCESS_TOKEN}"}

        # Make the HTTP GET request
        endpoint_response = requests.get(endpoint, headers=headers)
        product_detail = endpoint_response.json()
        response = {
            "product_detail": product_detail,
        }

        return jsonify(response)
