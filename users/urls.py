from django.urls import path
from users import views
urlpatterns=[
    path("index/",views.Home.as_view(),name="home"),
    path("accounts/signup",views.SignUpView.as_view(),name="signup"),
    path("accounts/signin", views.SingnInView.as_view(), name="signin"),



]