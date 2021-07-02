from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name='account'
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
