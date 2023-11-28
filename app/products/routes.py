from flask import jsonify, request
from app.products import bp
import requests
from config import Config


# Define the callback route for handling the OAuth response
@bp.route('/api/products', methods=["GET"])
def import_list_products():
    if request.method == "GET":
        # API endpoint to fetch list of products.
        endpoint = 'https://app.staging.zendrop.com/api/oauth-import-list-products'

        # Set up the headers with the Bearer token
        headers = {'Authorization': f"Bearer {Config.API_ENDPOINT_ACCESS_TOKEN}"}

        # Make the HTTP GET request
        endpoint_response = requests.get(endpoint, headers=headers)
        products_data = endpoint_response.json()
        response = {
            "products_data": products_data,
        }

        return jsonify(response)


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
