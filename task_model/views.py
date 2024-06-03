from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def add_task(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm()
        return render(request, 'task.html', {'form':form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')

def update_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(request.POST, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task.html', {'form':form})