from django.db import models
from django.forms import ModelForm, Textarea
# Create your models here.
from django.contrib.auth.models import User

class QuestionsModel(models.Model):
    qTitle = models.CharField(max_length = 25)
    qDescription = models.CharField(max_length = 75)

    def __str__(self):
        return self.qTitle + self.qDescription
    def isLiked(self, user1):
        return self.likes_set.filter(user=user1) and True or False


class QuestionModelForm(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ('qTitle', 'qDescription')
        widgets = {
           'qTitle': Textarea(attrs={'cols': 80, 'rows': 5}),
           'qDescription' :Textarea(attrs={'cols': 80, 'rows': 20}), 
           
        }
        
class ComentModel(models.Model):
    cText = models.CharField(max_length = 25)
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.cText
 
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE)
