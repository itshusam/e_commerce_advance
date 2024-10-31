from flask import jsonify, request
from services.product_service import create_product, get_product, update_product, delete_product
from flask import request, jsonify
from models.schemas.product_schema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from caching import cache
from utils import role_required

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


@role_required('admin')
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product_save = productService.save(product_data)
    if product_save:
        return product_schema.jsonify(product_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": product_data}), 400

@cache.cached(timeout=60)
def find_all():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    paginated_products = productService.find_all(page, per_page)
  
    return jsonify({
        "products": products_schema.dump(paginated_products.items),
        "total": paginated_products.total,
        "page": paginated_products.page,
        "pages": paginated_products.pages
    }), 200
