import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from questions.forms import QuestionForm
from questions.models import Dislike, Like, Question

logging.basicConfig(level=logging.DEBUG)

class QuestionView(View):
  form_class = QuestionForm
  initial = {}
  template_name = 'create_question.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class()
    context = {"form":form, "act_createq":True}
    return render(request, self.template_name, context=context)

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      title = request.POST.get("title")
      description = request.POST.get("description")
      new_question = Question.objects.create(title=title, description=description, user=request.user)
      new_question.save()
    questions = Question.objects.all()
    questions.reverse()
    context =  {'questions':questions, "act_allq":True}
    return render(request, 'home.html', context=context)

  @login_required(login_url="/login")
  def edit_ques(request):
    question_id = request.POST.get('question')
    question = Question.objects.get(id=int(question_id))
    context = { "question_title":question.title,
                "question_desc":question.description ,
                'question':question}
    return render(request, "update_question.html", context=context)

  @login_required(login_url="/login")
  def like(request):
    new_like, created = Like.objects.get_or_create(user=request.user, question_id=request.POST.get('question'))
    if not created:
      logging.debug("User already likes")
    else:
      try :
        d = Dislike.objects.get(user=request.user, question=request.POST.get('question'))
        d.delete()
      except ObjectDoesNotExist:
        logging.debug("User has'nt disliked it !!!")
      logging.debug("User likes now")
    questions = Question.objects.all()
    return render(request, 'home.html', {"questions":questions})

  @login_required(login_url="/login")
  def dislike(request):
      new_like, created = Dislike.objects.get_or_create(user=request.user, question_id=request.POST.get('question'))
      if not created:
         logging.debug("User already dislikes")
      else:
         try:
          l1 = Like.objects.get(user=request.user, question=request.POST.get('question'))
          l1.delete()
         except ObjectDoesNotExist:
          logging.debug("User hasn't dislike it yet!!!")
         logging.debug("User dislikes now")
      questions = Question.objects.all()
      return render(request, 'home.html', {"questions":questions})
