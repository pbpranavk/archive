from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

from .models import QuestionModelForm,QuestionsModel,ComentModel,Likes

def createQues(request):
    if request.method == "POST":
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            ques = form.save()
            quesList = QuestionsModel.objects.all() 
            return render(request, 'questionList.html', {"quesList":quesList})
    else:
        form = QuestionModelForm()
    return render(request, 'createQuestion.html', {'form':form})       
 

def searchposts(request):
    quesList = QuestionsModel.objects.all() 
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(qTitle__icontains=query) | Q(qDescription__icontains=query)

            results= QuestionsModel.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton,
                     "quesList":quesList
                     }

            return render(request, 'questionList.html', context)
  
        else:
            return render(request, 'questionList.html')

    else:
        return render(request, 'questionList.html')

def addComment(request):
    quesList = QuestionsModel.objects.all() 
    if request.method == 'GET':
        cT= request.GET.get('c')
        question = request.GET.get('question')
        qPK = QuestionsModel.objects.get(pk=question) 
        submitbutton= request.GET.get('submitc')
        filt = Q(question=qPK)
        prevComments = ComentModel.objects.filter(filt)
        if cT is not None:
            #lookups= Q(qTitle__icontains=query) | Q(qDescription__icontains=query)

            cM = ComentModel(cText=cT,question = qPK)            

            cM.save()
            

            context={
                     'submitbutton': submitbutton,
                     "quesList":quesList,
                     "prevComments":prevComments,
                     "question":question,
                     }

            return render(request, 'questionList.html', context)
 
        else:
            return render(request, 'questionList.html')

    else:
        return render(request, 'questionList.html')    
#@login_required(login_url='/loginTest/login/')
def like(request):
    try:
        new_like, created = Likes.objects.get_or_create(user = request.user, question_id = request.POST.get('question'))
        if not created:
            print("User already likes")
        else:
            print("User likes now")
        quesList = QuestionsModel.objects.all() 
        return render(request, 'questionList.html', {"quesList":quesList})
    except:
        return redirect('/loginTest/login')
            