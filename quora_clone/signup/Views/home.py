from django.shortcuts import render
from questions.models import Question
from django.views import View

class HomeView(View):
    def home(request):
        questions = Question.objects.all()
        questions.reverse()
        context = {'questions': questions, "act_allq" : True}
        return render(request, 'home.html', context=context)