from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=160)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='username',
        primary_key=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "%s" % self.title


class Answer(models.Model):
    text = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='username',
        primary_key=False,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null = True
    )

    def __str__(self):
        return self.text



class Comment(models.Model):
    text = models.CharField(max_length=25)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='username',
        primary_key=False,
    )

    def __str__(self):
        return self.text



class AnswerComment(models.Model):
    text = models.CharField(max_length=25)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='username',
        primary_key=False,
    )

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class CommentDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
