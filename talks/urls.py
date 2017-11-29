from __future__ import absolute_import 
from django.conf.urls import include, url

from . import views

# list_patterns =[
# 	'',
	
# ]

urlpatterns = [
	url(r'lists/$', views.TalkListDetailView.as_view(), name='detail'),
]