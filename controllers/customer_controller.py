from flask import jsonify, request
from services.customer_service import create_customer, get_customer, update_customer, delete_customer

def create_customer_controller():
    data = request.get_json()
    customer = create_customer(data)
    return jsonify(customer.serialize()), 201

def get_customer_controller(customer_id):
    customer = get_customer(customer_id)
    return jsonify(customer.serialize()), 200 if customer else ({"error": "Customer not found"}, 404)

def update_customer_controller(customer_id):
    data = request.get_json()
    customer = update_customer(customer_id, data)
    return jsonify(customer.serialize()), 200 if customer else ({"error": "Customer not found"}, 404)

def delete_customer_controller(customer_id):
    customer = delete_customer(customer_id)
    return ({"message": "Customer deleted successfully"}, 200) if customer else ({"error": "Customer not found"}, 404)
