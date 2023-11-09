import uuid

from flask import Blueprint, request, jsonify

products_bp = Blueprint('products', __name__)

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


@products_bp.route('/api/trending_products', methods=['GET', 'POST'])
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
