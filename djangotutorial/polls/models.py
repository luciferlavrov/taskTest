from django.db import models


class Task(models.Model):

    name = models.CharField(default='',max_length=200)
    description = models.TextField(default='')