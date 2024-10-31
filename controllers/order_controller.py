from flask import jsonify, request
from services.order_service import create_order, get_order, delete_order
from models.schemas.order_schema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache
from utils import role_required


def create_order_controller():
    data = request.get_json()
    order = create_order(data)
    return jsonify(order.serialize()), 201

def get_order_controller(order_id):
    order = get_order(order_id)
    return jsonify(order.serialize()), 200 if order else ({"error": "Order not found"}, 404)

def delete_order_controller(order_id):
    order = delete_order(order_id)
    return ({"message": "Order deleted successfully"}, 200) if order else ({"error": "Order not found"}, 404)

@role_required
def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    order_save = orderService.save(order_data)
    if order_save:
        return order_schema.jsonify(order_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": order_data}), 400

@cache.cached(timeout=60)
def find_all():
    
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    paginated_orders = orderService.find_all(page, per_page)
    
    return jsonify({
        "orders": orders_schema.dump(paginated_orders.items),
        "total": paginated_orders.total,
        "page": paginated_orders.page,
        "pages": paginated_orders.pages
    }), 200