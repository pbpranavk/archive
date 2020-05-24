from django.test import TestCase,Client
from django.contrib.auth.models import User
class HomeTest(TestCase):

    def test_home(self):
        self.client = Client()
        response = self.client.get(path = "/home")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All Questions")
        self.assertTemplateUsed("home.html")
        response.user =  User.objects.create_user(username="test_user", email="test@..", password = "testpassword")
        response = self.client.get(path = "/home")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All Questions")
        self.assertTemplateUsed("home.html")

