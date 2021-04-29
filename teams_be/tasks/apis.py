from rest_framework import mixins, viewsets

from teams_be.base import response
from teams_be.base.apis.mixins import MultipleSerializerMixin
from teams_be.tasks.models import Task
from teams_be.tasks.serializers import TaskSerializer, TaskResponseSerializer


class TaskViewSet(
    MultipleSerializerMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TaskResponseSerializer
    queryset = Task.objects.all()

    serializer_classes = {
        "create": TaskSerializer,
        "update": TaskSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task_obj = serializer.save()
        response_serializer = self.serializer_class(
            task_obj, context=self.get_serializer_context()
        )
        return response.Created(response_serializer.data)




