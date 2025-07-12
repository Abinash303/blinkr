from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('<str:code>/', views.redirect_short, name='redirect_short'),
    
]
