from django.urls import path
from . import views

app_name = 'task1'

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.game_list, name='game_list'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
]