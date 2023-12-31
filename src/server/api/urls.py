from django.urls import path
from api import views
from django.urls import path
from django.views.decorators.cache import cache_page
app_name = 'api'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('request/', views.request_friend, name='request'),
    path('accept/', views.accept_friend_request, name='accept'),
    path('compute/', views.compute_lalg_expression, name='lalg'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_study/', views.create_study, name='create_study'),
    path('join_study/', views.join_book_study, name='join_study'),
    ]
