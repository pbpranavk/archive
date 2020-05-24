from django.contrib import admin
from .models import QuestionsModel,ComentModel,Likes# Register your models here.
admin.site.register(QuestionsModel)
admin.site.register(ComentModel)
admin.site.register(Likes)