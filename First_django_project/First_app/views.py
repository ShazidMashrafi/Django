from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView,  CreateView, UpdateView, DeleteView
from First_app import models
from django.urls import reverse_lazy

def index_test(request):
    return HttpResponse('Hello World')

class IndexView(ListView):
   context_object_name = 'musician_list'
   model = models.Musician
   template_name = 'First_app/index.html'

class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'First_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'First_app/musician_form.html'

class UpdateMusician(UpdateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'First_app/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('First_app:index')
    template_name = 'First_app/delete_musician.html'