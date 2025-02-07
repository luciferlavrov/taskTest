from django.db import models

"42"
class Task(models.Model):

    name = models.CharField(default='',max_length=200)
    description = models.TextField(default='')