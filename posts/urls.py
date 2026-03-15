from django.urls import path

from .views import HomePageView, redirect_view

urlpatterns = [
        path("", redirect_view, name="redirect_to_home"),
        path("home/", HomePageView.as_view(), name="home"),
    ]
