from django.shortcuts import render
from django import forms
from django.forms import ModelForm, MultipleChoiceField
from .models import Problem,Tags, Articles
from django.http import HttpResponse
# Create your views here.
from django.forms.models import ModelChoiceIterator, ModelChoiceField

from django.forms import ModelForm

class tell(ModelForm): 
    class Meta:
        model = Problem
        fields = ['desc'] 

def tell_view(request):
        if request.method == "POST":
                form = tell(request.POST)
                if form.is_valid() :
                        pdesc = request.POST.get('desc')
                        prob = Problem(desc = pdesc, user =  request.user)
                        prob.save()
                        return render(request, "prob1.html", {'prob' : prob})                                                
        else:
                #print("Hi1111")
                form = tell()
        return render(request, "probm.html", {'form' : form})                                                

def show(request):
    return     HttpResponse()

class TagsForm(ModelForm):
        class Meta:
                model = Tags
                fields = ['tag']
def createTag(request):
        if request.method == "POST":
                form = TagsForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponse("Tag created")
        else:
                form = TagsForm()
        return render(request, "tag1.html" ,{"form" : form})                                

class ArticlesForm(ModelForm):
        opts =  [[x.id, x.tag] for x in Tags.objects.all()]      
        tags = MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                choices = opts
        )
        class Meta:
                model = Articles
                fields = ['title' , 'desc' , 'tags']

def createArticle(request):
        if request.method == "POST":
                form = ArticlesForm(request.POST)
                if form.is_valid():
                        title = request.POST.get('title')
                        desc =  request.POST.get('desc')
                        tags =  request.POST.getlist('tags') 
                        print(request.POST)
                        article = Articles.objects.create(title=title, desc = desc )
                        Tags1 = []
                        #article.save()
                        #Tag1 = Tags.objects.get(pk = tag1)
                        print(tags)
                        for x in tags :
                                tpr =  Tags.objects.get(pk = (int(x)))
                                print(tpr)
                                Tags1.append(tpr)
                        #article.tag.add(Tag1)
                        print(Tags1)
                        for t in Tags1:
                                article.tag.add(t)
                        #print(article)        
                        article.save()
                        return HttpResponse("Article created")
        else:
                form = ArticlesForm()
        return render(request, "article1.html" ,{"form" : form})                                
