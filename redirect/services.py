from links.models import Link


def get_destination_url(slug):
    destination_url = Link.objects.get(slug=slug).destination_url
    return destination_url
