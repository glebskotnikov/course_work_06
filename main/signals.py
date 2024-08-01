from django.contrib.auth import user_logged_in
from django.core.cache import cache
from django.dispatch import receiver


@receiver(user_logged_in)
def clear_cache_on_login(sender, user, request, **kwargs):
    try:
        cache.delete(f'total_mailings_{user.email}')
        cache.delete(f'active_mailings_{user.email}')
        cache.delete(f'unique_clients_{user.email}')
    except Exception as e:
        print(f"Error clearing cache: {e}")
