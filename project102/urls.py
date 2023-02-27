"""project102 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_list/',school_list.as_view(),name='school_list'),
    path('Homepage/',Homepage.as_view(),name='Homepage'),
    path('school_form/',school_form.as_view(),name='school_form'),

    re_path('^update/(?P<pk>\d+)/',school_update.as_view(),name='update'),
    re_path('^delete/(?P<pk>\d+)/',school_delete.as_view(),name='delete'),


    re_path('(?P<pk>\d+)/',School_detail.as_view(),name='details'),
]
