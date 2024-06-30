from django.urls import path

from rest_client import views

urlpatterns = [
    path('', views.process, name='process'),
    path('search/', views.search, name='search'),
    path('process/', views.process, name='process'),
    path('send/', views.send, name='send'),
]
