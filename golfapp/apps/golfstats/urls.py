from django.conf.urls import patterns, url

import views as views

urlpatterns = patterns('',
    url(r'list/golfer/', views.listGolfers, name='golfstats.list-golfers'),
    url(r'list/course/', views.listCourses, name='golfstats.list-courses'),
    url(r'^modify_golfer/(?P<golfer_id>(\d+))', views.modifyGolferForm, {}, name='golfstats.modify-golfer'),
    url(r'^add_golfer/', views.addGolferForm, {}, name='golfstats.add-golfer'),
    url(r'^modify_course/(?P<course_id>(\d+))', views.modifyCourseForm, {}, name='golfstats.modify-course'),
    url(r'^add_course/', views.addCourseForm, {}, name='golfstats.add-course'),
)
