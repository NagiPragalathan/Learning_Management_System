from django.urls import path
from . import views
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


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
        