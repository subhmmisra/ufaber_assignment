from collections import defaultdict

from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from teams_be.projects.serializers import ProjectBaseSerializer
from teams_be.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'start_date', 'end_date', 'project']

    def validate_start_date(self, value):
        if value < timezone.now().date():
            raise ValidationError("Can not create task in past")
        return value

    def validate(self, attrs):
        validation_errors = defaultdict(list)
        if attrs["end_date"] < attrs["start_date"]:
            validation_errors["end_date"].append(
                "End Date could not be before Start Date"
            )

        # Raise all errors at once
        if validation_errors:
            raise ValidationError(validation_errors)

        return super().validate(attrs)



class TaskResponseSerializer(serializers.ModelSerializer):
    project = ProjectBaseSerializer()

    class Meta(TaskSerializer):
        model = Task
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'project']

