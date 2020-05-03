from django.urls import path
from main_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('hate', views.hate, name='hate'),
    path('love', views.love, name='love'),
    path('listings/', views.list, name='list'),
    path('messages/', views.messages, name='messages'),
    path('new-listing/', views.new_list, name='new-listing'),
    path('profile/', views.profile, name='profile')
]
