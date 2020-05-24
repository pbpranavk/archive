from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Problem(models.Model):
    desc = models.CharField(max_length = 50)
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        to_field = 'username',
        primary_key = False,

    ) 
    def __str__(self) :
        return "%s" % self.desc 

class Tags(models.Model):
    tag = models.CharField( max_length=25)

    def __str__(self):
        return self.tag


class Articles(models.Model):
    title =models.CharField( max_length=25)
    desc = models.CharField( max_length=50)

    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title
     
