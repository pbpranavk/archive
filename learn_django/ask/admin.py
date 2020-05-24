from django.contrib import admin

# Register your models here.

from .models import Problem, Tags, Articles# Register your models here.
admin.site.register(Problem)
admin.site.register(Tags)
admin.site.register(Articles)
