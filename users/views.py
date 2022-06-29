from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegistrationForm,LoginForm
from django.views.generic import CreateView,FormView,TemplateView
from users.models import User
from django.urls import reverse_lazy

from django.contrib.auth import authenticate,login,logout
class Home(TemplateView):
    template_name = "index.html"
class SignUpView(CreateView):
    model=User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("signin")


class SingnInView(FormView):
    model=User
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if not user:
                return render(request,"login.html",{"form":form})
            login(request,user)
            if request.user.is_candidate:
                return redirect("cand-home")
            else:
                return redirect("emp-home")



