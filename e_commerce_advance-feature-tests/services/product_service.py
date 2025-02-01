from models.product import Product
from app import db

def create_product(data):
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_product(product_id):
    return Product.query.get(product_id)

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if product:
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        db.session.commit()
    return product

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
    return product
