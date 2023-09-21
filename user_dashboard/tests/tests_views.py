from django.test import TestCase, Client
from django.urls import reverse
from user_dashboard.models import Support  # noqa
from django.contrib.auth.models import User


class TestSupportPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.login(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('user-support', args=[self.user.profile.id])

    def test_support_message(self):
        post_data = {
            'user': self.user,
            'title': 'test message',
            'description': 'test message description'
        }

        self.assertTrue(self.user.is_authenticated)

        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(Support.objects.count(), 1)
