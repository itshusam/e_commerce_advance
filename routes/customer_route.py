from flask import Blueprint
from controllers.customer_controller import create_customer_controller, get_customer_controller, update_customer_controller, delete_customer_controller

customer_bp = Blueprint('customer', __name__)

customer_bp.route('/customers', methods=['POST'])(create_customer_controller)
customer_bp.route('/customers/<int:customer_id>', methods=['GET'])(get_customer_controller)
customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])(update_customer_controller)
customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])(delete_customer_controller)
