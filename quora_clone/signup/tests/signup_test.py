from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .login_logout_test import Login_Logout_Test
from signup.views.sign_up import SignUpView
from pprint import pprint as pp
from selenium import webdriver

class SignupTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='testuser123')
        user.set_password('12345')
        user.save()
        self.driver = webdriver.Firefox()


    def test_signup(self):
        response = self.client.login(username = "testuser123", password = "12345")
        self.assertTrue(response)
        response = self.client.get('/home')
        self.assertContains(response, "testuser123")
        self.client.logout()
        self.driver.get("http://localhost:8000/signup/")
        self.driver.find_element_by_id('id_username').send_keys("test123")
        self.driver.find_element_by_id('id_password1').send_keys("12345")
        self.driver.find_element_by_id('id_password2').send_keys("")
        self.driver.find_element_by_id('id_submit').click()

    def tearDown(self):
        self.driver.close()
        #pass