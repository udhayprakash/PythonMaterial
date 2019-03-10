# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Passenger(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=50)