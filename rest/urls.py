from django.urls import path
from rest import views

urlpatterns = [
    path('', views.index, name='index'),
]
