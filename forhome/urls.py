from django.urls import path
from forhome import views

urlpatterns = [
    path('forhome', views.forhome, name='forhome'),
]
