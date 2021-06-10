from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('library.urls'), name='library'),
    path('admin/', admin.site.urls)
]
