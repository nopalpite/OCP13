from django.shortcuts import render


def index(request):
    """
    View function for the index page.
    """
    return render(request, 'index.html')


def page_not_found(request, exception):
    """
    View function for handling the 404 (Page not found) error.
    """
    return render(request, '404.html', status=404)


def server_error(request):
    """
    View function for handling the 500 (Server error) error.
    """
    return render(request, '500.html', status=500)
