from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=120,blank=True,null=True)
    text=models.TextField()
    created_time=models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title



