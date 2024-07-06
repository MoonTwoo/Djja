from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('index', views.index),
    path('contact', views.contact),
    path('enot', views.enot),
]