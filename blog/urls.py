from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns ('',

	#I should rewrite with more intelegent of build-in views 
	url(r'^tag/(?P<tag_pk>\d+)$', views.IndexView.as_view(), name="tag"),
	url(r'^thread/(?P<thread_pk>\d+)$', views.IndexView.as_view(), name="thread"),
	url(r'^$', views.IndexView.as_view(), name="index"),


	
	url(r'^record/(?P<pk>\d+)$', views.record, name="record"),

	url(r'^like$', views.like, name="like"),


)