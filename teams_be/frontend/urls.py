from django.urls import path

from teams_be.frontend import views

urlpatterns = [
	path('', views.list, name="list"),
	path('project', views.project_detail, name="list"),
	path('projects/<uuid:pk>', views.project_detail, name="project_detail"),
	path('projects/<uuid:p_pk>/tasks/<uuid:t_pk>', views.task_detail, name="task_detail"),
	path('projects/<uuid:p_pk>/tasks/edit/<uuid:t_pk>', views.task_edit, name="task_edit"),


]