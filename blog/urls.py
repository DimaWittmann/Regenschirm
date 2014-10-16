from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns ('',
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^tag/(?P<tag>\w+)$', views.IndexView.as_view(), name="tag"),
	url(r'^record/(?P<pk>\d+)$', views.RecordView.as_view(), name="record"),


)