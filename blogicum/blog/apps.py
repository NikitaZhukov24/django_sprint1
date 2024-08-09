"""Module apps blog."""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """App config class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
