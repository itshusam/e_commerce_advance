from flask import jsonify, request
from services.customer_account_service import create_customer_account, get_customer_account, update_customer_account, delete_customer_account

def create_customer_account_controller():
    data = request.get_json()
    account = create_customer_account(data)
    return jsonify(account.serialize()), 201

def get_customer_account_controller(account_id):
    account = get_customer_account(account_id)
    return jsonify(account.serialize()), 200 if account else ({"error": "Account not found"}, 404)

def update_customer_account_controller(account_id):
    data = request.get_json()
    account = update_customer_account(account_id, data)
    return jsonify(account.serialize()), 200 if account else ({"error": "Account not found"}, 404)

def delete_customer_account_controller(account_id):
    account = delete_customer_account(account_id)
    return ({"message": "Account deleted successfully"}, 200) if account else ({"error": "Account not found"}, 404)
