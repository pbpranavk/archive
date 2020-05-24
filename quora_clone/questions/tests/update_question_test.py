from django.test import TestCase
from questions.views.update_question import UpdateQuestion
from django.contrib.auth.models import AnonymousUser, User
from questions.models import Question
from django.http import HttpRequest

class update_question_testcase(TestCase):
    def setUp(self):
        user= User.objects.create(username="test_user", email="test@..")
        user.set_password("testpassword")
        self.user = user
        q1 = Question.objects.create(
            title= "How to get a visa",
            description = "I am a student..What all documents would I need",
            user = self.user)

    def test_update_question_pass(self):
        request = HttpRequest()
        request.user = self.user
        request.POST['new_question_title'] = "How to get a visa for work?"
        request.POST['new_question_description'] = "Am no longer a student...What should I do?"
        q1 = Question.objects.get(title = "How to get a visa")
        request.POST['question'] = q1.title
        response = UpdateQuestion.update_question(request)
        q2 = Question.objects.all().first()
        self.assertEqual(q2.title, "How to get a visa for work?")
        self.assertEqual(q2.description, "Am no longer a student...What should I do?")

    # def test_update_question_faile(self):
    #     request = HttpRequest()
    #     request.user = User.objects.create_user(username="bad_test_user", email="bad_test@..", password = "badtestpassword")
    #     request.POST['qT'] = "How to get a visa for work?"
    #     request.POST['qD'] = "Am no longer a student...What should I do?"
    #     q1 = Question.objects.get(title = "How to get a visa")

    #     request.POST['q'] = q1

    #     response = UpdateQuestion.update_question(request)
    #     q2 = Question.objects.all().first()
    #     self.assertEqual(q2.title, "How to get a visa")
    #     self.assertEqual(q2.description, "I am a student..What all documents would I need")
    #     self.assertContains(response, "You can edit questions which are created by you")
