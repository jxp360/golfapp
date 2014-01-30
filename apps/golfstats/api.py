from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from apps.golfstats.models import Golfer, GolfCourse

class GolferResource(ModelResource):
    class Meta:
        queryset = Golfer.objects.all()
        resource_name = 'golfer'
        authorization = Authorization()

class GolfCourseResource(ModelResource):
    class Meta:
        queryset = GolfCourse.objects.all()
        resource_name = 'golfcourse'
        authorization = Authorization()

