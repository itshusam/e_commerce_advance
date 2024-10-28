from flask import jsonify, request
from services.product_service import create_product, get_product, update_product, delete_product

def create_product_controller():
    data = request.get_json()
    product = create_product(data)
    return jsonify(product.serialize()), 201

def get_product_controller(product_id):
    product = get_product(product_id)
    return jsonify(product.serialize()), 200 if product else ({"error": "Product not found"}, 404)

def update_product_controller(product_id):
    data = request.get_json()
    product = update_product(product_id, data)
    return jsonify(product.serialize()), 200 if product else ({"error": "Product not found"}, 404)

def delete_product_controller(product_id):
    product = delete_product(product_id)
    return ({"message": "Product deleted successfully"}, 200) if product else ({"error": "Product not found"}, 404)
