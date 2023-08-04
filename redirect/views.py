from django.shortcuts import redirect

from redirect.services import get_destination_url


def redirect_view(request, slug):
    destination_url = get_destination_url(slug)
    return redirect(destination_url)
