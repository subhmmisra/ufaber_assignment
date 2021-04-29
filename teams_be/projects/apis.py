from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from teams_be.base import response
from teams_be.base.apis.mixins import MultipleSerializerMixin
from teams_be.base.apis.pagination import paginated_response
from teams_be.projects.models import Project
from teams_be.projects.serializers import ProjectCreateUpdateSerializer, ProjectResponseSerializer
from teams_be.tasks.serializers import TaskResponseSerializer
from teams_be.tasks.services import project_tasks


class ProjectViewSet(
    MultipleSerializerMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class =ProjectResponseSerializer
    queryset = Project.objects.all()

    serializer_classes = {
        "create": ProjectCreateUpdateSerializer,
        "update": ProjectCreateUpdateSerializer,
        "tasks": TaskResponseSerializer
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task_obj = serializer.save()
        response_serializer = self.serializer_class(
            task_obj, context=self.get_serializer_context()
        )
        return response.Created(response_serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task_obj = serializer.save()
        response_serializer = self.serializer_class(
            task_obj, context=self.get_serializer_context()
        )
        return response.Ok(response_serializer.data)

    @action(methods=["GET"], detail=True, url_path="tasks")
    def tasks(self, request, *args, **kwargs):
        project_obj = self.get_object()
        tasks = project_tasks(project_obj)

        serializer = paginated_response(
            request, tasks, self.get_serializer_class(), extra_context=self.get_serializer_context()
        )
        return response.Ok(serializer.data)





