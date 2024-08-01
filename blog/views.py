from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'object_list'
    extra_context = {"title": "Блоги"}

    def get_queryset(self):
        data = None
        if settings.CACHE_ENABLED:
            data = cache.get('blog_list')

        if not data:
            data = super().get_queryset()
            if settings.CACHE_ENABLED:
                cache.set('blog_list', data, 60 * 60)

        return data


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        blog_id = self.kwargs.get(self.pk_url_kwarg)
        cache_key = f'blog_detail_{blog_id}'
        data = None

        if settings.CACHE_ENABLED:
            data = cache.get(cache_key)

        if not data:
            data = super().get_object(queryset)

        # Увеличиваем счетчик просмотров независимо от того, откуда были получены данные
        data.views_count += 1
        data.save()

        # Кэшируем данные, если кэш включен
        if settings.CACHE_ENABLED:
            cache.set(cache_key, data, 60 * 60)

        return data


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        cache.delete('blog_list')  # очистка кэша после создания новой записи блога
        return response


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        response = super().form_valid(form)
        blog_id = self.kwargs.get(self.pk_url_kwarg)
        cache.delete('blog_list')
        cache.delete(f'blog_detail_{blog_id}')
        return response

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def test_func(self):
        return self.request.user.groups.filter(name='content-manager').exists() or \
            self.request.user.is_superuser


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        cache.delete('blog_list')  # очистка кэша после удаления записи блога
        return response

    def test_func(self):
        return self.request.user.groups.filter(name='content-manager').exists() or \
            self.request.user.is_superuser
