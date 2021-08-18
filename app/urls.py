from django.urls import path
from . import views

urlpatterns =  [
    path('', views.resume, name='home'),
    path('create-message/', views.createMessage, name='create-message'),
    path('inbox/', views.inbox, name='inbox'),
    path('view-message/<str:pk>/', views.viewMessage, name='view-message'),
]