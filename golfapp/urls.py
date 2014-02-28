from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apps.golfstats.api import GolferResource, GolfCourseResource
import apps.golfstats.views as gviews
import apps.piffycup.views as pcviews
import apps.golfstats.urls as gsurls
import apps.piffycup.urls as pcurls
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

v1_0_api = Api(api_name='v1_0')
v1_0_api.register(GolferResource())
v1_0_api.register(GolfCourseResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'golfapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^golfstats/golfers/$', golfers.golfers, name='golfers'),
    url(r'^$', TemplateView.as_view(template_name='templates/base.html'), name='index'), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_0_api.urls)),
    url(r'^piffycup/', include(pcurls)),
    url(r'^golfstats/', include(gsurls)),
    
)
