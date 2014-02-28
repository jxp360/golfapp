#!/usr/bin/env python
import os, sys
import django

sys.path.append("/data/workspace/golfapp")
os.environ['DJANGO_SETTINGS_MODULE'] = "golfapp.settings.dev"

from golfapp.apps.golfstats import models

golfers = [('Jeff Pfeiffenberger', 'jxp360', 'jxp360@gmail.com', '8453433437'),
 ('ABCDEFGH', 'temp123', 'AJSKFJSDLK', '23423423432'),
 ('3ABCDEFGH', 'temp432', '7AJSKFJSDLK', '57523423423432'),
 ('4ABCDEFGH', 'pffuy34', '6AJSKFJSDLK', '123423423423432'),
 ('5ABCDEFGH', 'jpfeif', '8AJSKFJSDLK', '231433423423432'),
]

def dropall():
    models.Golfer.objects.all().delete()
    

if __name__ == "__main__":
    print models.Golfer.objects.all()
    for golfer in golfers:
        temp = models.Golfer(name=golfer[0], username=golfer[1], email=golfer[2], phone=golfer[3])
        temp.save()
   
    print models.Golfer.objects.all()

