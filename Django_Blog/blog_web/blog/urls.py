from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login,name='login'),
    path('signup/',views.sign,name='signup'),
    path('signup/signup/',views.sign,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('home/my_post/',views.my_post,name='my_post'),
    path('logout/',views.user_logout,name='logout'),
    path('home/my_post/<int:pk>/delete/', views.delete_post, name='delete-post'),
]
