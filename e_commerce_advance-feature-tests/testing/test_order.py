import unittest
from unittest.mock import patch
from app import app

class TestOrderEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('services.order_service.place_order')
    def test_place_order(self, mock_place_order):
        mock_place_order.return_value = {"id": 1, "order_date": "2023-01-01", "customer_id": 1, "items": [{"product_id": 1, "quantity": 2}]}
        response = self.client.post('/orders', json={"customer_id": 1, "items": [{"product_id": 1, "quantity": 2}]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["order_date"], "2023-01-01")

    @patch('services.order_service.get_order')
    def test_get_order(self, mock_get_order):
        mock_get_order.return_value = {"id": 1, "order_date": "2023-01-01", "customer_id": 1, "items": [{"product_id": 1, "quantity": 2}]}
        response = self.client.get('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["order_date"], "2023-01-01")

if __name__ == '__main__':
    unittest.main()
