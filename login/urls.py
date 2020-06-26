from django.urls import path, re_path, include
from login import views

urlpatterns = [
    path('', views.tel_number, name='tel_login'),
    path('first_user/', views.first_user, name='first_user'),
    path('new_user/', views.new_user, name='new_user'),
]