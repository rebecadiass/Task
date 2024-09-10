from django.views.generic import ListView, CreateView, DeleteView
from .models import Task
from django.urls import reverse_lazy 
from django.shortcuts import get_object_or_404, redirect

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')



    