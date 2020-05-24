from questions.forms import AnswerForm
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from questions.models import Question, Answer, AnswerComment
from django.contrib.auth.decorators import login_required

class AnswerView(View):
  form_class = AnswerForm
  initial = {}
  template_name = "answer_view.html"

  @login_required(login_url="/login")
  def get(self, request, *args, **kwargs):
    form = self.form_class()
    question_id = request.GET['question_id']
    question = Question.objects.get(id=question_id)
    context = {"form":form, "question":question}
    return render(request,self.template_name, context=context)

  @login_required(login_url="/login")
  def post(self, request, *args, **kwargs):
    question_id = request.POST['question_id']
    answer_text = request.POST['answer_text']
    question = Question.objects.get(id=question_id)
    ans = Answer.objects.create(text=answer_text, question=question, user=request.user)
    ans.save()
    return render(request, "question_details.html", {"question":question})

  @login_required(login_url="/login")
  def add_answer_comment(request):
    text = request.POST['comment_text']
    answer_id = request.POST['answer_id']
    question = request.POST['question']
    answer = Answer.objects.get(id=answer_id)
    answer_comment = AnswerComment.objects.create(text=text, answer=answer, user=request.user)
    answer_comment.save()
    question = Question.objects.get(title=question)
    return render(request, "question_details.html", {"question":question})
