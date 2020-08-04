import markdown2
from django.http import HttpResponse, JsonResponse

from . import util


def index(request):
    """List of all available wiki entries."""
    return JsonResponse({
        "entries": util.list_entries()
    })


def display_entry(request, title):
    """Read a file, convert content to HTML, and display."""
    content = util.get_entry(title)
    if content:
        return JsonResponse({
            "content": markdown2.markdown(content)
        })
    return JsonResponse({})
