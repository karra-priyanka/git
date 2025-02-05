from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

# View for displaying all tasks
def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# View for adding a new task
def add_task(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm()
    return render(request, 'todo/add_task.html', {'form': form})

# View for deleting a task
def delete_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.delete()
    return redirect('index')

# View for marking a task as completed
def complete_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')
