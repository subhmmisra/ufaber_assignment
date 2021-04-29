from teams_be.tasks.models import Task

## service function to fetch the task of a specific project
def project_tasks(project_obj):
    tasks = Task.objects.filter(project=project_obj.id)
    return tasks