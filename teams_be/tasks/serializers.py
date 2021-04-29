from rest_framework import serializers

from teams_be.projects.serializers import ProjectBaseSerializer
from teams_be.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'start_date', 'end_date', 'project']

class TaskResponseSerializer(serializers.ModelSerializer):
    project = ProjectBaseSerializer()

    class Meta(TaskSerializer):
        model = Task
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'project']

