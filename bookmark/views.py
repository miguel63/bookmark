from django.shortcuts import render
from django.views.generic.list import ListView  #목록뷰
from .models import Bookmark
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields =['site_name', 'url']
    success_url =reverse_lazy('list')
    template_name_suffix ='_create'

class BookmarkDetailView(DetailView):
    model =Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DetailView):
    model = Bookmark
    success_url = reverse_lazy('list')



# Create your views here.
