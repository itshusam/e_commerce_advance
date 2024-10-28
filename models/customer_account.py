from app import db
from sqlalchemy.orm import relationship

class CustomerAccount(db.Model):
    __tablename__ = 'customer_accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="customer_account")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "customer_id": self.customer_id
        }
