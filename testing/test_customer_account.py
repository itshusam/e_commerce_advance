import unittest
from unittest.mock import patch
from app import app

class TestCustomerAccountEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('services.customer_account_service.create_customer_account')
    def test_create_customer_account(self, mock_create_customer_account):
        mock_create_customer_account.return_value = {"id": 1, "username": "johndoe"}
        response = self.client.post('/customer-accounts', json={"username": "johndoe", "password": "securepassword", "customer_id": 1})
        self.assertEqual(response.status_code, 201)
        self.assertIn("johndoe", response.get_json()["username"])

    @patch('services.customer_account_service.get_customer_account')
    def test_get_customer_account(self, mock_get_customer_account):
        mock_get_customer_account.return_value = {"id": 1, "username": "johndoe", "customer_id": 1}
        response = self.client.get('/customer-accounts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("johndoe", response.get_json()["username"])

if __name__ == '__main__':
    unittest.main()
