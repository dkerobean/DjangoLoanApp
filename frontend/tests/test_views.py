from django.test import TestCase, Client
#from frontend.models import LoanApplication
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoanApplication(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(
            username='testuser',
            password='testpassword',
        )

    def test_loan_details(self):
        self.url = reverse('loan-details')
        post_data = {
            'loan_type': 'test_loan',
            'finance_type': 'test_finance',
            'loan_amount': '600.00',
            'loan_duration': '34'
            }

        self.assertTrue(self.user.is_authenticated)

        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, 302)

