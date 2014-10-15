from django.conf.urls import patterns, include, url

from django.contrib import admin
from monitor.state import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^cpu/$', views.state_cpu),
    url(r'^port/$', views.state_port),
    url(r'^state/$', views.state),
    url(r'^netstat/$', views.state_netstat),
)
