from django.test import TestCase, Client
from django.contrib.auth.models import User
class Login_Logout_Test(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='testuser123')
        user.set_password('12345')
        user.save()


    def test_login_success(self):
        resp = self.client.login(username = "testuser123", password = "12345")
        self.assertTrue(resp)

    def test_login_failure(self):
        resp = self.client.login(username = "testuser123sadf", password = "12345")
        self.assertFalse(resp)

    def test_logout(self):
        response = self.client.login(username = "testuser123", password = "12345")
        self.assertTrue(response)
        response = self.client.get('/home')
        self.assertContains(response, "testuser123")
        self.client.logout()
        response = self.client.get('/home')
        self.assertTrue('testuser123' not in response)

