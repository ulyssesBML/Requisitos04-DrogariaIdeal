"""DrogariaIdeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^login/$', views.show_login, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/', views.register, name="register"),
    url(r'^self_edit/', views.self_edit_user, name="self_edit_user"),
    url(r'^list_user_edit/', views.list_user_edit, name="list_user_edit"),
    url(r'^edit_user/(?P<user_id>[0-9]+)/',views.edit_user,name="edit_user"),
    url(r'^list_user_delete/',views.list_user_delete,name="list_user_delete"),
    url(r'^delete_user/(?P<user_id>[0-9]+)/',views.delete_user,name="delete_user"),
    url(r'^register_client/', views.register_client, name="register_client"),
    url(r'^self_edit/', views.self_edit_client, name="self_edit_client"),


]
