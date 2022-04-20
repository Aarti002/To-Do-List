"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #app urls
    path('index', views.index, name="index"),
    path('', views.login_user, name="login_user"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('dologin', views.dologin, name="dologin"),
    path('register_user', views.register_user, name="register_user"),
    path('register_user_save', views.register_user_save, name="register_user_save"),
    path('add_new_todo', views.add_new_todo, name="add_new_todo"),
    path('save_new_todo', views.save_new_todo, name="save_new_todo"),
    path('edit_todo_item/<str:todo_id>', views.edit_todo_item, name="edit_todo_item"),
    path('edit_todo_save', views.edit_todo_save, name="edit_todo_save"),
    path('remove_todo/<str:todo_id>', views.remove_todo, name="remove_todo"),
path('filter_todo', views.filter_todo, name="filter_todo"),
]
