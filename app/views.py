from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class school_list(ListView):
    model=School
    context_object_name='sc'
    template_name='app/school_list.html'
    queryset=School.objects.all()
    order=['name']

class School_detail(DetailView):
    model=School
    context_object_name='sc'

class Homepage(TemplateView):
    template_name='app/Homepage.html'

class school_form(CreateView):
    model=School
    fields='__all__'


class school_update(UpdateView):
    model=School
    fields='__all__'

class school_delete(DeleteView):
    model=School
    context_object_name='sc'
    success_url=reverse_lazy('school_list')