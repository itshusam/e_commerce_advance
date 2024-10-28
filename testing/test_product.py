import unittest
from unittest.mock import patch
from app import app

class TestProductEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('services.product_service.create_product')
    def test_create_product(self, mock_create_product):
        mock_create_product.return_value = {"id": 1, "name": "Widget", "price": 9.99}
        response = self.client.post('/products', json={"name": "Widget", "price": 9.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Widget", response.get_json()["name"])

    @patch('services.product_service.get_product')
    def test_get_product(self, mock_get_product):
        mock_get_product.return_value = {"id": 1, "name": "Widget", "price": 9.99}
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Widget", response.get_json()["name"])

if __name__ == '__main__':
    unittest.main()
