from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from ..models import Question
from django.http import HttpResponse

class UpdateQuestion(View):
    def update_question(request):
        new_question_title = request.POST.get("new_question_title")
        new_question_description = request.POST.get("new_question_description")
        question_text = request.POST.get("question")
        question = Question.objects.get(title=question_text)
        question.title = new_question_title
        question.description = new_question_description
        question.save()
        return redirect("/home")
