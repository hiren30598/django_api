from django.conf.urls import url, include

# from users.views import UserCreate

urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/register', UserCreate.as_view() , name="user_create_api"),
]