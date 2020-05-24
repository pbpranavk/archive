import logging

from django.test import TestCase, Client
from django.contrib.auth.models import AnonymousUser, User
from questions.models import Question
from questions.views.questions_view import QuestionView
#from selenium.webdriver.firefox.webdriver import WebDriver
from django.http import HttpRequest

logging.basicConfig(level=logging.DEBUG)

class QuestiontestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user", email="test@..")
        user.set_password("testpassword")
        user.save()
        self.user = user
        Question.objects.create(title="How to get a visa", description="I am a student..What all documents would I need", user=self.user)
        self.client = Client()

    def test_create_question(self):
        data= {}
        data['title'] = "A dummy question"
        data['description'] = "Some description"
        self.client.login(username="test_user", password="testpassword")
        response = self.client.post("/questions/create_question",data)
        self.assertEqual(response.status_code,200)
        #logging.info(response.content)
        self.assertContains(response, "A dummy question")

    def test_edit_question(self):
        request = HttpRequest()
        request.user = self.user
        q = Question.objects.get(title="How to get a visa")
        request.POST['question'] = q.id
        response = QuestionView.edit_ques(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user)

    def test_like(self):
        request = HttpRequest()
        request.user = self.user
        test_q = Question.objects.get(title="How to get a visa")
        request.POST['question'] = test_q.id

        response = QuestionView.like(request)
        self.assertEqual(test_q.like_set.all().count(),1)

        response = QuestionView.like(request)
        self.assertEqual(test_q.like_set.all().count(),1)

        request.user = User.objects.create_user(username="second_test_user", email="second_test@..", password = "secondtestpassword")
        response = QuestionView.like(request)
        self.assertEqual(test_q.like_set.all().count(),2)

        response = QuestionView.dislike(request)
        self.assertEqual(test_q.like_set.all().count(),1)


    def test_dislike(self):
        request = HttpRequest()
        request.user = self.user
        test_q = Question.objects.create(
            title="Another Question",
            description="Another question describtion" ,
            user=self.user)
        request.POST['question'] = test_q.id

        response = QuestionView.dislike(request)
        self.assertEqual(test_q.dislike_set.all().count(),1)

        response = QuestionView.dislike(request)
        self.assertEqual(test_q.dislike_set.all().count(),1)

        request.user = User.objects.create_user(username="second_test_user", email="second_test@..", password="secondtestpassword")
        response = QuestionView.dislike(request)
        self.assertEqual(test_q.dislike_set.all().count(),2)

        response = QuestionView.like(request)
        self.assertEqual(test_q.dislike_set.all().count(),1)


