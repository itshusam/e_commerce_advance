from flask import jsonify, request
from services.order_service import create_order, get_order, delete_order

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
