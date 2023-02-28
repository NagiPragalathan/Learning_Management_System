from django.urls import path
from LMS import settings
from django.conf.urls.static import static

from .Routes.common import *
from .Routes.staff import *
from .Routes.students import *
from .Routes.study import *
from .Routes.admin_page import *


urlpatterns = [
    path('', base),
    path('home', home),


    path('chat_lobby', lobby),
    path('room/', video_chat_room),
    path('get_token/', getToken),

    path('create_member/', createMember),
    path('get_member/', getMember),
    path('delete_member/', deleteMember),

    path('login',login_page),
    path('login_to_home',login_into_home),


    path('add_Faculty',add_faculty),
    path('add_usr',add_usr),

    path('personal_detials',Personal_detials),


    path('chat_home/', chat_home),
    path('<str:room>/', chat_room, name="chat_room"),
    path('chat_home/checkview', checkview, name="checkview"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),

    path('class_room',home_classroom),
    path('message/<str:room>/',chatgetMessages, name="message"),
    path('<str:pk>/<str:class_id>',nave_home_classroom),
    path('add_class',add_class),
    path("save_added_class",save_add_class),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
        