from django.db import models

from teams_be.base.models import TimeStampedUUIDModel


class Project(TimeStampedUUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    duration = models.SmallIntegerField(default=0)


