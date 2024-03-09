from django.urls import re_path as url
from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses$', views.courses, name='courses'),
]