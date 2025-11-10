from django.contrib import admin
from django.urls import path, include
from students.views import home_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', home_redirect, name='home'),
]