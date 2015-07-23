from django.conf.urls import patterns, url
from apps.surveys import views

urlpatterns = patterns('', 
	url(r'^process/$', views.frame, name='frame'),
	url(r'^$', views.index, name='index'),
)