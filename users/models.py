from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    country = models.CharField(max_length=35, verbose_name="страна", **NULLABLE)

    token = models.CharField(max_length=100, verbose_name="token", **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name="статус пользователя", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ["email"]
        permissions = [
            ("can_view_users", "Can view users"),
            ("can_change_is_active", "Can change is_active status"),
        ]

    def __str__(self):
        return self.email

    def is_manager(self):
        return self.groups.filter(name="manager").exists()
