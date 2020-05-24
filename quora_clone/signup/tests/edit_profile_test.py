from django.test import TestCase
from signup.views.edit_profile import EditProfileView
from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser, User

class EditProTest(TestCase):
    def setUp(self):
        user = User.objects.create( username = "testuser" , email = "testuser@..", password = "password")
        self.user = user

    def test_edit_pro(self):
        request = HttpRequest()
        request.user = self.user
        request.POST['fname'] = "Test First Name"
        request.POST['lname'] = "Test Last Name"
        request.method = "POST"
        response = EditProfileView.edit(request)
        u = User.objects.get(username = "testuser")
        self.assertEqual(u.first_name,"Test First Name" )
        self.assertEqual(u.last_name,"Test Last Name" )