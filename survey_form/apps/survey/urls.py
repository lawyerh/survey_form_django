from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^process$', views.process),
	url(r'^goback$', views.goback),
	url(r'^results$', views.results),
	url(r'^$', views.index)

]