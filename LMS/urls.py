from django.contrib import admin
from django.urls import path, include

app_name = 'myapp' # add this line to define your app_name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
    
]