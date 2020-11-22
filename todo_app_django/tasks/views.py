from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect

from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    # grab all
    tasks = Task.objects.all()
    form = TaskForm()
    # pass natin sa template through the context
    # context syntax creating a dictionary context = {'task':task}
    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    # then ipasa natin sa views para magamit natin sa template using {% tasks %}
    return render(request, 'tasks/index.html', context)


def updateTask(request, pk):
    # throw the primary key in the url

    # render(pasa mo sa template, yung url)
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        # instance=task we're updating the instance of this item
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'task': task, 'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    itemToDelete = Task.objects.get(id=pk)
    context = {'itemToDelete': itemToDelete}
    if request.method == "POST":
        itemToDelete.delete()
        return HttpResponseRedirect('/')
    return render(request, 'tasks/delete.html', context)
