from django.urls import re_path
from . import views


#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^other/$', views.other, name='other'),
    re_path(r'^relative/$', views.relative, name='relative')
]