from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

class Validator(models.Manager):
    def is_valid(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be more than 5 characters"
            print errors
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog desc should be more than 10 characters"
            print errors
        return errors;

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    desc = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Validator()

#  mac$ python manage.py makemigrations
#  $ python manage.py migrate
#  python manage.py shell
# from apps.Courses.models import *
# >>> Courses.objects.all()
