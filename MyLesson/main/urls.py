from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('lesson1', views.lesson1, name='lesson1'),
    path('lesson2', views.lesson2, name='lesson2'),
]
