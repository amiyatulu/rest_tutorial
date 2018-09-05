from django.urls import re_path, path, include
from . import views

urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
]