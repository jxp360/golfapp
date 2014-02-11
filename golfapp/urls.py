from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apps.golfstats.api import GolferResource, GolfCourseResource
import apps.golfstats.views as gviews
import apps.piffycup.views as pcviews
import apps.piffycup.urls as pcurls
from django.contrib import admin
admin.autodiscover()

v1_0_api = Api(api_name='v1_0')
v1_0_api.register(GolferResource())
v1_0_api.register(GolfCourseResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'golfapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_0_api.urls)),
    #url(r'^golfstats/golfers/$', golfers.golfers, name='golfers'),
    url(r'^piffycup/', include(pcurls)),
)
