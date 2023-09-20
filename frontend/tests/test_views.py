from django.test import TestCase, Client
from frontend.models import LoanApplication
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
        # self.assertRedirects(response, reverse('loan-details'))

    def test_personal_details(self):
        self.url = reverse('personal-details')
        post_data = {
            'dob': 'test_dob',
            'marital_status': 'test_status',
            'mobile_number': '4534564645',
            'address': 'test_address',
            'city': 'test_city',
            'postal_code': 'test_postal_code',
            }

        self.assertTrue(self.user.is_authenticated)

        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('document-upload'))

    def test_document_upload(self):
        self.url = reverse('document-upload')
        post_data = {
            'user': self.user,
            'loan_type': 'test_loan',
            'finance_type': 'test_finance',
            'loan_amount': '600.00',
            'loan_duration': '34',
            'dob': 'test_dob',
            'marital_status': 'test_status',
            'mobile_number': '4534564645',
            'address': 'test_address',
            'city': 'test_city',
            'postal_code': 'test_postal_code',
            'id_card': 'id-proof'

        }

        self.assertTrue(self.user.is_authenticated)
        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, 302)

        self.assertTrue(LoanApplication.objects.count(), 1)
