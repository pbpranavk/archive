from django.contrib import admin
from .models import Tag,Question,Like,CommentLike,Comment,Dislike
# Register your models here.


admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Like)
admin.site.register(CommentLike)
admin.site.register(Comment)
admin.site.register(Dislike)