from django.urls import path
from .views import ProfileView, image_upload_ajax, user_site

app_name = 'profile'

urlpatterns = [
    path('<user>/image/', image_upload_ajax, name='image_upload'),
    path('<user>/user_site/', user_site, name='user_site'),
    path('<user>', ProfileView.as_view(), name='user-profile'),
]
