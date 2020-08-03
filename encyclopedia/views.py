from django.http import HttpResponse, JsonResponse

from . import util


def index(request):
    """List of all available wiki entries."""
    return JsonResponse({"entries": util.list_entries()})
