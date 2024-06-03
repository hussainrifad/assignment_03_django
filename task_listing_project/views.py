from django.shortcuts import render
from task_model.models import TaskModel

def home(request):
    tasks = TaskModel.objects.all()
    isTasks = 0
    if len(tasks) != 0:
        isTasks = len(tasks)
    return render(request, 'home.html', {'tasks':tasks, 'isTasks':isTasks })