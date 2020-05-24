from django.test import TestCase
from questions.views.search_view import SearchView
from questions.models import Question
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

class SearchTest(TestCase):
    def setUp(self):
        user, created = User.objects.get_or_create(username="test_user", email="test@..")
        if not created:
            user.set_password("testpassword")
        self.user = user
        q, q_created = Question.objects.get_or_create(title="How to get a visa", description="I am a student..What all documents would I need", user = self.user)
        if not q_created:
            q1 = q
        else:
            q1 = q_created


    def test_search_posts_found(self):
        request = HttpRequest()
        request.GET['query'] = "visa"
        request.GET['submit'] = "Search"
        request.method = "GET"
        #print(request.GET.get('q'))
        response = SearchView.searchposts(request)
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How to get a visa")

    def test_search_posts_notfound(self):
        request = HttpRequest()
        request.GET['query'] = "not there sadfasdf"
        request.GET['submit'] = "Search"
        request.method = "GET"
        #print(request.GET.get('q'))
        response = SearchView.searchposts(request)
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No search results for this query")

    def test_search_posts_querynone(self):
        request = HttpRequest()
        #request.GET['q'] = "not there sadfasdf"
        request.GET['submit'] = "Search"
        request.method = "GET"
        #print(request.GET.get('q'))
        response = SearchView.searchposts(request)
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nothing Found !!!")
