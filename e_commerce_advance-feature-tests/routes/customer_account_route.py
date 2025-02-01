from flask import Blueprint
from controllers.customer_account_controller import create_customer_account_controller, get_customer_account_controller, update_customer_account_controller, delete_customer_account_controller

customer_account_bp = Blueprint('customer_account', __name__)

customer_account_bp.route('/customer_accounts', methods=['POST'])(create_customer_account_controller)
customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['GET'])(get_customer_account_controller)
customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['PUT'])(update_customer_account_controller)
customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['DELETE'])(delete_customer_account_controller)
