from rest_framework import serializers

from teams_be.projects.models import Project

class ProjectBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name','description', 'duration']

class ProjectResponseSerializer(ProjectCreateUpdateSerializer):
    class Meta(ProjectCreateUpdateSerializer):
        model = Project
        fields = ['id'] + ProjectCreateUpdateSerializer.Meta.fields
