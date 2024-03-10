from django.urls import re_path as url
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]