from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        cache.delete(f'unique_clients_{user.id}')
        return response


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {"title": "Клиенты"}

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(owner=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if (
                obj.owner == self.request.user
                or self.request.user.is_superuser
        ):
            return obj
        else:
            raise Http404


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        user = self.request.user
        response = super().form_valid(form)
        cache.delete(f'unique_clients_{user.id}')
        return response


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        response = super().delete(request, *args, **kwargs)
        cache.delete(f'unique_clients_{user.id}')
        return response

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not self.request.user.is_superuser and obj.owner != self.request.user:
            raise Http404
        return obj
