import logging

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from questions.models import CommentDislike, CommentLike, Comment, Question

logging.basicConfig(level=logging.DEBUG)

class Comments(View):
    @login_required(login_url="/login")
    def add_comment(request):
        '''
        Describing request.
        Response: Values in context
        Logic

        if required :
             Example Req Resp
        '''
        questions = Question.objects.all()
        if request.method == 'GET':
            comment_text= request.GET.get('comment_text')
            question_id = request.GET.get('question_id')
            submitbutton = request.GET.get("submitc")
            question = Question.objects.get(pk=question_id)
            if comment_text is not None:
                new_comment = Comment(text=comment_text,question=question, user=request.user)
                new_comment.save()
                context = {
                        'submitbutton': submitbutton,
                        "questions":questions,
                        "question":question,
                        }
                return render(request, 'home.html', context)
            else:
                return render(request, 'home.html')
        else:
            return render(request, 'home.html')

    @login_required(login_url="/login")
    def comment_like(request):
        new_like, created = CommentLike.objects.get_or_create(user=request.user, comment_id=request.POST.get('comment'))
        if not created:
                logging.debug("User already likes")
        else:
            try :
                d = CommentDislike.objects.get(user=request.user, comment_id=request.POST.get('comment'))
                d.delete()
            except ObjectDoesNotExist:
                logging.debug("User has'nt disliked it !!!")
        questions = Question.objects.all()
        return render(request, 'home.html', {"questions":questions})

    @login_required(login_url="/login")
    def comment_dislike(request):
        new_like, created = CommentDislike.objects.get_or_create(user=request.user, comment_id=request.POST.get('comment'))
        if not created:
            logging.debug("User already dislikes")
        else:
            try:
                l1 = CommentLike.objects.get(user=request.user, comment_id=request.POST.get('comment'))
                l1.delete()
            except ObjectDoesNotExist:
                logging.debug("User hasn't liked it yet!!!")
        questions = Question.objects.all()
        return render(request, 'home.html', {"questions":questions})
