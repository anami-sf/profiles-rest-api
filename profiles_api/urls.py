from django.urls import path

from profiles_api import views


ulrpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
]

