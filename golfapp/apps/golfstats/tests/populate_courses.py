#!/usr/bin/env python
import os, sys
import django

sys.path.append("/data/workspace/golfapp")
os.environ['DJANGO_SETTINGS_MODULE'] = "golfapp.settings.dev"

from golfapp.apps.golfstats import models

course_info = [('Pine Ridge Golf Course', '123 Main Street', '83823923892938'),
 ('5ABCDEFGH', 'jpfeif', '231433423423432'),
]

def dropall():
    models.GolfCourse.objects.all().delete()
    models.GolfCourseInfo.objects.all().delete()
    models.CourseHole.objects.all().delete()

if __name__ == "__main__":
    dropall()
    print models.GolfCourseInfo.objects.all()

    for course in course_info:
        temp = models.GolfCourseInfo(name=course[0], address=course[1], phonenumber=course[2])
        temp.save()
   
    gc = models.GolfCourseInfo.objects.get(name=course_info[0][0])

    temp = models.GolfCourse(tees="BLACK", number_of_holes=18, slope=123.3, rating=71.3)
    temp.golfcourse = gc
    temp.save()
    temp = models.GolfCourse( tees="WHITE", number_of_holes=18, slope=125.3, rating=70.3)
    temp.golfcourse = gc
    temp.save()

    gc = models.GolfCourse.objects.get(tees='WHITE')

    temp = models.CourseHole(number=13, par=4, yards=389.0, handicap=15)
    temp.course = gc
    temp.save()

    print models.GolfCourseInfo.objects.all()
    print models.GolfCourse.objects.all()
    print models.CourseHole.objects.all()

