from django.test import TestCase, Client
from questions.models import Comment, CommentLike, CommentDislike,Question
from django.http import HttpRequest
from questions.views.comments_view import Comments
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import logout, login
from django.conf import settings
from importlib import import_module

class CommentTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user", email="test@..")
        user.set_password("testpassword")
        user.save()
        self.user = user
        self.client = Client()
        q = Question.objects.create(
            title= "How to get a visa",
            description = "I am a student..What all documents would I need",
            user = self.user)
        self.q = q

    def test_add_comment_test_success(self):
        data = {}
        data['comment_text'] = "It is very easy first get a passport!!!"
        data['question_id'] = self.q.id
        data['submitc'] = "Submit"
        self.client.login(username = "test_user", password ="testpassword")
        response = self.client.get('/questions/add_comment/',data, follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"It is very easy first get a passport!!!" )

    def test_add_comment_test_failure(self):
        data = {}
        data['c'] = "It is very easy first get a passport!!!"
        data['question_id'] = self.q.id
        data['submitc'] = "Submit"
        response = self.client.get('/questions/add_comment/',data, follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response,"It is very easy first get a passport!!!" )

    def test_add_comment_test_non_loggedin(self):
        request = HttpRequest()
        request.method = "GET"
        request.GET['c'] = "It is very easy first get a passport!!!"
        request.GET['question'] = Question.objects.all().first().id
        request.GET['submitc'] = "Submit"
        request.user = self.user
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        login(request, self.user)
        logout(request)
        try:
            Comments.add_comment(request)
            self.assertTrue(False)
        except  KeyError as err:
            print(err)
            self.assertTrue(True)

    def test_comment_like_test(self):
        request = HttpRequest()
        request.user = self.user
        Comment.objects.create(text="First comment", user=self.user, question=Question.objects.all().first())
        request.POST['comment'] = Comment.objects.get(text = "First comment").id
        response = Comments.comment_like(request)
        c = Comment.objects.all().first()
        self.assertEqual(c.commentlike_set.all().count() , 1)
        response = Comments.comment_like(request)
        c = Comment.objects.all().first()
        self.assertEqual(c.commentlike_set.all().count() , 1)
        request.user = User.objects.create_user(username="second_test_user", email="second_test@..", password="secondtestpassword")
        response = Comments.comment_like(request)
        c = Comment.objects.all().first()
        self.assertEqual(c.commentlike_set.all().count() , 2)
        response = Comments.comment_dislike(request)
        c = Comment.objects.all().first()

        self.assertEqual(c.commentlike_set.all().count() , 1)


    def test_comment_dislike_test(self):
        request = HttpRequest()
        request.user = self.user
        request.POST['comment'] = Comment.objects.create(text="Second comment", question=Question.objects.all().first(), user=self.user).id
        response = Comments.comment_dislike(request)
        c = Comment.objects.get(text = "Second comment")
        self.assertEqual(c.commentdislike_set.all().count() , 1)
        response = Comments.comment_dislike(request)
        c = Comment.objects.get(text = "Second comment")
        self.assertEqual(c.commentdislike_set.all().count() , 1)
        request.user = User.objects.create_user(username="second_test_user", email="second_test@..", password="secondtestpassword")
        response = Comments.comment_dislike(request)
        c = Comment.objects.get(text = "Second comment")
        self.assertEqual(c.commentdislike_set.all().count() , 2)
        response = Comments.comment_like(request)
        c = Comment.objects.get(text = "Second comment")
        self.assertEqual(c.commentlike_set.all().count() , 1)
