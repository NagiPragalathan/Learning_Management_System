from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),

    path('chat_lobby', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),

    path('login',views.login_page),


    path('add_Faculty',views.add_faculty),
    path('add_usr',views.add_usr),



]