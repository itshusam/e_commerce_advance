import unittest
from unittest.mock import patch
from app import app

class TestCustomerEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('services.customer_service.create_customer')
    def test_create_customer(self, mock_create_customer):
        mock_create_customer.return_value = {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "1234567890"}
        response = self.client.post('/customers', json={"name": "John Doe", "email": "john@example.com", "phone": "1234567890"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("John Doe", response.get_json()["name"])

    @patch('services.customer_service.get_customer')
    def test_get_customer(self, mock_get_customer):
        mock_get_customer.return_value = {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "1234567890"}
        response = self.client.get('/customers/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("John Doe", response.get_json()["name"])

    @patch('services.customer_service.update_customer')
    def test_update_customer(self, mock_update_customer):
        mock_update_customer.return_value = {"id": 1, "name": "Jane Doe", "email": "jane@example.com", "phone": "0987654321"}
        response = self.client.put('/customers/1', json={"name": "Jane Doe", "email": "jane@example.com", "phone": "0987654321"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Jane Doe", response.get_json()["name"])

    @patch('services.customer_service.delete_customer')
    def test_delete_customer(self, mock_delete_customer):
        mock_delete_customer.return_value = {"message": "Customer deleted successfully"}
        response = self.client.delete('/customers/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted successfully", response.get_json()["message"])

if __name__ == '__main__':
    unittest.main()
