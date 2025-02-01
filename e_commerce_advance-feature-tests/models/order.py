from app import db
from sqlalchemy.orm import relationship

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = relationship("Customer")
    products = relationship("Product", secondary="order_products")

    def serialize(self):
        return {
            "id": self.id,
            "order_date": self.order_date,
            "customer_id": self.customer_id,
            "products": [product.serialize() for product in self.products]
        }

class OrderProduct(db.Model):
    __tablename__ = 'order_products'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
