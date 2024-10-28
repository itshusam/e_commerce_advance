from flask import Blueprint
from controllers.order_controller import create_order_controller, get_order_controller, delete_order_controller

order_bp = Blueprint('order', __name__)

order_bp.route('/orders', methods=['POST'])(create_order_controller)
order_bp.route('/orders/<int:order_id>', methods=['GET'])(get_order_controller)
order_bp.route('/orders/<int:order_id>', methods=['DELETE'])(delete_order_controller)