# sam_education/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  
    path('users/', include('apps.users.urls')),]
