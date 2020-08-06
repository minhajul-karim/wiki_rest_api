import json
import markdown2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from . import util


@api_view(['GET'])
def api_overview(request):
    """Gives the overview of this api."""
    api_urls = {
        "List": "/entries/",
        "Detail View": "/entries/<str:title>/",
        "Create": "/entries/",
        "Update": "/entries/<str:title>/",
    }
    return Response(api_urls)


@api_view(["GET", "POST"])
def entries_list(request):
    """List of all available wiki entries."""
    if request.method == "GET":
        return Response({
            "entries": util.list_entries()
        })
    elif request.method == "POST":
        title = request.data["title"].lower()
        content = request.data["content"]
        pages = util.list_entries()
        if title in pages:
            return Response({
                "page_exists": True
            })
        util.save_entry(title, content)
        return Response({
            "page_exists": False
        })


@api_view(["GET", "PUT"])
def entry_detail(request, title):
    """Read a file, convert content to HTML, and display."""
    if request.method == "GET":
        content = util.get_entry(title)
        if content:
            return Response({
                "title": title,
                "content": markdown2.markdown(content)
            })
        return Response({})
    elif request.method == "PUT":
        title = request.data["title"].lower()
        content = request.data["content"]
        util.save_entry(title, content)
        return Response({
            "title": title,
            "content": content
        })
