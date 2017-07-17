# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    name = models.CharField(max_length= 250)
    phone = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=30, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)






