from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'frontend/list.html')


def project_detail(request, pk):
    return render(request, 'frontend/details.html')

def task_detail(request, p_pk, t_pk):
    return render(request, 'frontend/task_detail.html')

def task_edit(request, p_pk, t_pk):
    return render(request, 'frontend/edit_task.html')