from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class EditProfileView(View):
    def edit(request):
        if request.method == "POST":
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            user = request.user
            user.first_name = fname
            user.last_name = lname
            user.save()
            return  redirect(reverse_lazy("signup:edit_pro"))
        context = {"user" : request.user, "act_editq": True}
        return render(request, "edit_profile.html", context=context)
