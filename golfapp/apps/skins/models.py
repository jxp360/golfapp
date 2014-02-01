from django.db import models
from golfstats.models import GolfCourse, Golfer

class SkinsInfo(models.Model):
    course = GolfCourse()
    golfers = models.ManyToMany(Golfer)
    date = models.DateTime()
    results = SkinResult

class SkinResult(models.Model):
    game = SkinsInfo()
    holes = models.FloatInteger()
    golfer = Golfer()

