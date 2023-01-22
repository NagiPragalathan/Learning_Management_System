from django.urls import path
from . import views, cource
from LMS import settings
from django.conf.urls.static import static


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
    path('login_to_home',views.login_into_home),


    path('add_Faculty',views.add_faculty),
    path('add_usr',views.add_usr),

    path('personal_detials',views.Personal_detials),

    path('generate_cource',cource.Agri),

    path('chatbot',views.chatbot),


    path('chat_home/', views.chat_home),
    path('<str:room>/', views.room, name="room"),
    path('chat_home/checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
        