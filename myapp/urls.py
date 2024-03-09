from django.urls import re_path as url
from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses$', views.courses, name='courses'),
    url(r'^grades/(?P<course_id>\d+)/$', views.grades, name='grades'),
    url(r'^regrade/(?P<grade_id>\d+)/$', views.regrade, name='regrade'),
]