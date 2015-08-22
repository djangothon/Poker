from django.db import models

# Create your models here.

import datetime

# Create your models here.



class contacts(models.Model):
    contact_phasedout_age = models.DateTimeField(default=datetime.datetime.now)
    contact_name = models.CharField(max_length=64)
    contact_ph_num = models.CharField(max_length=13)
    contact_emailid = models.EmailField(max_length=100)
    contact_last_contacted = models.DateTimeField(null=True)

    # def __unicode__(self):
    #     return "%s, %s (%s)" % (self.city, self.statecode, self.zipcodeIntclass Meta:
    #     ordering = ['zipcode']
