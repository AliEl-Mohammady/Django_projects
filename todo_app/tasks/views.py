from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


def tasks(request):
    # return HttpResponse("Welcome to the Task list app")
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    context = {
        'tasks': tasks,
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'tasks/task.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(request.POST or None, instance=task)
    context = {
        'task': task,
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        form.save()
        # if request.is_ajax():
        #         return JsonResponse({"message": "Task updated successfully!"})
        return redirect('/')

    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete_task.html', {'task': task})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')