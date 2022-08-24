"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path
from devops.views import index as main_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_index, name='index'),
]

