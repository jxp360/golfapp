from django.db import models

class Golfer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    def __unicode__(self):
        return self.name

class GolfCourseInfo(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phonenumber =  models.CharField(max_length=14)
    def __unicode__(self):
        return self.name

class GolfCourse(models.Model):
    golfcourse = GolfCourseInfo()
    tees = models.CharField(max_length=10)
    number_of_holes = models.IntegerField()
    slope = models.FloatField()
    rating = models.FloatField()
    def __unicode__(self):
        return self.golfcourse.name
    
class CourseHole(models.Model):
    course = GolfCourse()
    number = models.IntegerField() 
    par = models.IntegerField()
    yards = models.FloatField()
    handicap = models.IntegerField()

class ScoreHole(models.Model):
    hole_info = CourseHole()
    score = models.IntegerField()

class Score(models.Model):
    golfcourse = GolfCourse()
    golfer = Golfer()
    holes = ScoreHole()
    date = models.DateField()

