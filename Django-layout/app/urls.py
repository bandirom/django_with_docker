from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
