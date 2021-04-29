from rest_framework.routers import DefaultRouter

from teams_be.projects.apis import ProjectViewSet
from teams_be.tasks.apis import TaskViewSet

default_router = DefaultRouter(trailing_slash=False)

default_router.register("projects", ProjectViewSet, basename="projects")
default_router.register("tasks", TaskViewSet, basename="tasks")
urlpatterns = default_router.urls
