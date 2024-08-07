from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from delivery.models import DeliveryAttempt
from mailings.forms import MailingForm, MessageForm, MailingManagerForm
from mailings.models import Mailing, Message


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailings:list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {"title": "Рассылки"}

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_manager():
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delivery_attempts"] = DeliveryAttempt.objects.filter(
            mailing=self.object
        )

        return context

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if (
                obj.owner == self.request.user
                or self.request.user.is_superuser
                or self.request.user.is_manager()
        ):
            return obj
        else:
            raise Http404


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    success_url = reverse_lazy("mailings:list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingForm
        elif user.has_perm("mailings.can_change_status"):
            return MailingManagerForm
        else:
            raise PermissionDenied

    def form_valid(self, form):
        user = self.request.user
        response = super().form_valid(form)
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return response


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailings:list")

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not self.request.user.is_superuser and obj.owner != self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        response = super().delete(request, *args, **kwargs)
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return response


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return response


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {"title": "Сообщения"}

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Message.objects.all()
        else:
            return Message.objects.filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if (
                obj.owner == self.request.user
                or self.request.user.is_superuser
                or self.request.user.is_manager()
        ):
            return obj
        else:
            raise Http404


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message-list")

    def form_valid(self, form):
        user = self.request.user
        response = super().form_valid(form)
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return response


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("mailings:message-list")

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not self.request.user.is_superuser and obj.owner != self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        response = super().delete(request, *args, **kwargs)
        cache.delete(f'total_mailings_{user.id}')
        cache.delete(f'active_mailings_{user.id}')
        return response
