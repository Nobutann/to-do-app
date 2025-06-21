from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()
    tasks = Task.objects.all() 
    context = {'tasks': tasks, 'TaskForm': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            
        return redirect('/')

    return render(request, 'index.html', context)
