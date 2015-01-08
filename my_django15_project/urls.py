from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_django15_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^astrologuesser/', include('astrologuesser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
