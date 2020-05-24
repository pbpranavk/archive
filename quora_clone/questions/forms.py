from django import forms
from django.forms import ModelForm, MultipleChoiceField, Textarea
from django.forms.models import ModelChoiceField, ModelChoiceIterator

from questions.models import Answer, Question, Tag


class  QuestionForm(ModelForm):
    title = forms.CharField(max_length=80, widget = Textarea(attrs={'cols': 80, 'rows': 5}))
    description  = forms.CharField(max_length=160, widget = Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(ModelForm):
    text = forms.CharField(max_length=50, required=True,  widget = Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Answer
        fields = ['text']
