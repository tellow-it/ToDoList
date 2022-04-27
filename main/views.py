from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from main.models import ToDo


# Create your views here.

class ToDoView(ListView):
    model = ToDo
    paginate_by = 5
    template_name = 'main/todolist.html'
    context_object_name = 'todo_list'
    queryset = ToDo.objects.all()


class ToDoDetail(DetailView):
    model = ToDo
    template_name = 'main/tododetail.html'
    success_url = '/'


class ToDoUpdate(UpdateView):
    model = ToDo
    fields = ['important', 'title', 'category', 'description', 'deadline']
    template_name = 'main/todoupdate.html'
    success_url = '/'


class ToDoCreate(CreateView):
    model = ToDo
    fields = ['important', 'title', 'slug', 'category', 'description', 'deadline']
    success_url = '/'
    template_name = 'main/todocreate.html'


class ToDoDelete(DetailView):
    model = ToDo
    template_name = 'main/tododelete.html'
    success_url = '/'

