from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^input/', hello.views.inputt, name='inputt'),
    url(r'^false/', hello.views.false, name='false'),
    url(r'^true/', hello.views.true, name='true'),
    url(r'^admin/', include(admin.site.urls)),
]
