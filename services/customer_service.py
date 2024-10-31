from models.customer import Customer
from app import db
from sqlalchemy import select
def create_customer(data):
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def get_customer(customer_id):
    return Customer.query.get(customer_id)

def update_customer(customer_id, data):
    customer = Customer.query.get(customer_id)
    if customer:
        customer.name = data.get("name", customer.name)
        customer.email = data.get("email", customer.email)
        customer.phone = data.get("phone", customer.phone)
        db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
    return customer


def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers
