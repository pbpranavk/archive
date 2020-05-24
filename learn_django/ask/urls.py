from django.urls import path,re_path


from . import views 

urlpatterns = [
    path('problems', views.tell_view),
    path('show' , views.show),
    path('createTag',views.createTag, name = 'createTag') ,
    path('createArticle', views.createArticle, name = 'createArticle')
]