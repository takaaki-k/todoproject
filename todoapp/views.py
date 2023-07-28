from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView

class TaskList(ListView):
  model = Task
  context_object_name = "tasks"
  
class TaskDetail(DetailView):
  model = Task
  context_object_name = "task"