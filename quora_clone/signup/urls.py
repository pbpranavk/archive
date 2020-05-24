from django.urls import path
from signup.views import edit_profile, home, sign_up

urlpatterns = [
    path('' , sign_up.SignUpView.as_view(), name = 'sup'),
    path('edit_pro', edit_profile.EditProfileView.edit, name = 'edit_pro')
]