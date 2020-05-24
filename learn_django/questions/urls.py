
from django.urls import path,re_path


from . import views 

urlpatterns = [
 path('questionList/', views.createQues),
 path('createQuestion/', views.createQues, name = 'createQues'),
 re_path(r'^$', views.searchposts, name = 'searchposts') ,
path('addComment/', views.addComment, name = 'addComment'),
path('like/', views.like,name= 'like')
]

