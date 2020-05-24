from questions.models import Question
from django.shortcuts import render

from questions.models import Question

class QuestionDetails:
    def details(request,question_id):
        question = Question.objects.get(id=question_id)
        return render(request, 'question_details.html', {"question":question} )