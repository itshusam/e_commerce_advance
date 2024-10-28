from models.order import Order, OrderProduct
from app import db

def create_order(data):
    new_order = Order(order_date=data['order_date'], customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    for product_id in data['product_ids']:
        order_product = OrderProduct(order_id=new_order.id, product_id=product_id)
        db.session.add(order_product)

    db.session.commit()
    return new_order

def get_order(order_id):
    return Order.query.get(order_id)

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
    return order
