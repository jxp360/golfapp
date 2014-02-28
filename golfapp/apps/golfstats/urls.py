from django.conf.urls import patterns, url

import views as views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'list.html', views.listGolfers, name='golfstats-list'),
    url(r'modify-golfer.html', views.modifyGolfers, name='golfstats-modify-golfer'),
    url(r'modify-golfer-form.html', views.modifyGolferForm, name='golfstats-modify-golfer-form'),
)
