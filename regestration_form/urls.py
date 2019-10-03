from django.urls import path ,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("login_fb/", views.login_fb, name="login_fb"),
    path("logout_fb/", auth_views.LogoutView.as_view(), name="logout_fb"),
    path("home_fb", views.home_fb, name="home_fb"),
    path('social/', include('social_django.urls', namespace="social")),
    path("index_google", views.index_google, name="index_google"),





]
