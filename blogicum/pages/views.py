"""This module provides views functions for pages app."""
from django.shortcuts import render


def about(request):
    """View function about."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """View function rules."""
    template = 'pages/rules.html'
    return render(request, template)
