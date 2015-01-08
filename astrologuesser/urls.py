from django.conf.urls import patterns, url
from astrologuesser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /astrologuesser/5/
    url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /astrologuesser/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /astrologuesser/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
