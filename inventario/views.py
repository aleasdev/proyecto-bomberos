from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *



#VISTA DE CAMIONES

class ListInv(ListView):
    model = Cabina
    template_name = "inventario.html"

class BlogCreateView(CreateView):
    model = Cabina
    template_name = "bombero_new.html"
    fields = ["nombre_cabina", "item", "elemento", "marca" ,"observaciones" ,"cantidad" ,"estado"]
    success_url = reverse_lazy ("informacion")

class BlogDetailView(DetailView):
    model = Cabina
    template_name = "bombero_detail.html"
    success_url = reverse_lazy ("informacion")

class BlogEditView(UpdateView):
    model = Cabina
    template_name = "bombero_edit.html"
    fields = ["item", "elemento", "marca" ,"observaciones" ,"cantidad" ,"estado"]
    success_url = reverse_lazy ("informacion")

class BlogDeleteView(DeleteView):
    model = Cabina
    template_name = "bombero_delete.html"
    success_url = reverse_lazy ("informacion")


    


# Create your views here.
