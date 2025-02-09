from flask import Blueprint
from controllers.product_controller import create_product_controller, get_product_controller, update_product_controller, delete_product_controller

product_bp = Blueprint('product', __name__)

product_bp.route('/products', methods=['POST'])(create_product_controller)
product_bp.route('/products/<int:product_id>', methods=['GET'])(get_product_controller)
product_bp.route('/products/<int:product_id>', methods=['PUT'])(update_product_controller)
product_bp.route('/products/<int:product_id>', methods=['DELETE'])(delete_product_controller)
