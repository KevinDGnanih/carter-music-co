""" Main app view """
from django.shortcuts import render


def handler404(request, exception):
    """ Error handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)
