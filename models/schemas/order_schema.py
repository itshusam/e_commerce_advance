from marshmallow import fields
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.DateTime(required=True)
    customer_id = fields.Integer(required=True)

    class Meta:
        fields = ("id", "order_date", "customer_id")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
