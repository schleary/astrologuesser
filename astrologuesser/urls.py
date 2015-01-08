from django.conf.urls import patterns, url

from astrologuesser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
