import unittest
from unittest.mock import patch
from app import app
import json

class MedTrackTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'healthy', response.data)

    @patch('services.dynamodb.DynamoDBService.get_patient_by_email')
    @patch('services.dynamodb.DynamoDBService.create_patient')
    def test_patient_registration_success(self, mock_create, mock_get_email):
        # Mock that email is not registered yet
        mock_get_email.return_value = None
        mock_create.return_value = (True, "Success")

        response = self.client.post('/api/auth/register/patient', json={
            'name': 'Test Patient',
            'email': 'patient@test.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('patient_id', data)

    @patch('services.dynamodb.DynamoDBService.get_doctor_by_email')
    def test_doctor_login_invalid(self, mock_get_email):
        # Mock that doctor is not found
        mock_get_email.return_value = None

        response = self.client.post('/api/auth/login', json={
            'role': 'Doctor',
            'email': 'doctor@test.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid email', response.data)

    def test_unauthorized_access(self):
        # Accessing protected route without session
        response = self.client.get('/api/patient/appointments')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
