from models.customer_account import CustomerAccount
from app import db

def create_customer_account(data):
    new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
    db.session.add(new_account)
    db.session.commit()
    return new_account

def get_customer_account(account_id):
    return CustomerAccount.query.get(account_id)

def update_customer_account(account_id, data):
    account = CustomerAccount.query.get(account_id)
    if account:
        account.username = data.get("username", account.username)
        account.password = data.get("password", account.password)
        db.session.commit()
    return account

def delete_customer_account(account_id):
    account = CustomerAccount.query.get(account_id)
    if account:
        db.session.delete(account)
        db.session.commit()
    return account
