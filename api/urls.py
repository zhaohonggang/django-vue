from django.conf.urls import url
from .views import UserLoginAPIView, request_user
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/login/$', UserLoginAPIView.as_view()),
    url(r'^api/request_user/$', request_user),
    url(r'^api-token-auth/', views.obtain_auth_token),
]