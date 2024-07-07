from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from clients.models import Client
from mailings.services import send_mailings


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('clients:list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('clients:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
