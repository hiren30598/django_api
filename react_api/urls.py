from django.conf.urls import url, include

from . import views


urlpatterns = [
	url(r'^hello/', views.HelloView.as_view() , name='hello'),
]