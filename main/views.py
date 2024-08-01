from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from django.conf import settings

from blog.models import Blog
from clients.models import Client
from mailings.models import Mailing


@login_required
def index(request):
    user_id = request.user.id

    total_mailings = None
    active_mailings = None
    unique_clients = None

    if settings.CACHE_ENABLED:
        total_mailings = cache.get(f"{user_id}_total_mailings")
        active_mailings = cache.get(f"{user_id}_active_mailings")
        unique_clients = cache.get(f"{user_id}_unique_clients")

    if total_mailings is None or active_mailings is None or unique_clients is None:
        if request.user.is_superuser or request.user.groups.filter(name="manager").exists():
            total_mailings = Mailing.objects.count()
            active_mailings = Mailing.objects.filter(status="started").count()
            unique_clients = (
                Client.objects.annotate(num_mailings=Count("mailings"))
                .filter(num_mailings__gt=0)
                .count()
            )
        else:
            total_mailings = Mailing.objects.filter(owner=request.user).count()
            active_mailings = Mailing.objects.filter(
                owner=request.user, status="started"
            ).count()
            unique_clients = (
                Client.objects.filter(mailings__owner=request.user)
                .annotate(num_mailings=Count("mailings"))
                .filter(num_mailings__gt=0)
                .count()
            )

        if settings.CACHE_ENABLED:
            cache.set(f"{user_id}_total_mailings", total_mailings, 60 * 60)
            cache.set(f"{user_id}_active_mailings", active_mailings, 60 * 60)
            cache.set(f"{user_id}_unique_clients", unique_clients, 60 * 60)

    random_blog_posts = Blog.objects.order_by("?")[:3]

    context = {
        "total_mailings": total_mailings,
        "active_mailings": active_mailings,
        "unique_clients": unique_clients,
        "random_blog_posts": random_blog_posts,
    }

    return render(request, "main/index.html", context)
