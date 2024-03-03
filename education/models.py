from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    speciality = models.CharField(max_length=12)
