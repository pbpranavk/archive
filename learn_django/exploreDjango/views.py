from django.shortcuts import render
from questions.models import QuestionsModel
from questions.views import createQues
def home(request):
    quesList = QuestionsModel.objects.all()

    context = {
        'quesList' : quesList
    }
    print(quesList)
    return render(request, 'home.html', context)