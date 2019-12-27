from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('create', views.UserCreate.as_view() , name="user_create_api"),
    url('', views.UserListView.as_view() , name="user_list_api"),
]