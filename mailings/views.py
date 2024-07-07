from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.models import Mailing, Message


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['send_time', 'send_frequency', 'status', 'start_datetime', 'end_datetime', 'clients']
    success_url = reverse_lazy('mailings:list')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['send_time', 'send_frequency', 'status', 'start_datetime', 'end_datetime', 'clients']
    success_url = reverse_lazy('mailings:list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:list')


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailings:message-list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailings:message-list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message-list')