from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm

def add_category(request):
    form = CategoryForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = CategoryForm()      
        return render(request, 'task.html', {'form':form})

def delete_category(request, id):
    return HttpResponse('Delete...')

def update_category(request, id):
    return HttpResponse('Update...')
