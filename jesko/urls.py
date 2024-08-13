from django.urls import path
from jesko import views

urlpatterns = [
    path('jesko', views.jesko, name='jesko')
]
