from django.db import models

from teams_be.base.models import TimeStampedUUIDModel
from teams_be.projects.models import Project


class Task(TimeStampedUUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects")
    #created_by = models.ForeignKey(User)

