from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField('Work')

    def __str__(self):
        return self.name

class Work(models.Model):
    link = models.CharField(max_length=255)
    work_type_choices = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )
    work_type = models.CharField(max_length=2, choices=work_type_choices)

    def __str__(self):
        return self.work_type