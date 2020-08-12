from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        # If url has query parameter name
        name = request.GET.get("page")
        if name:
            files = util.list_entries()
            possible_files = []
            for file in files:
                if name == file:
                    return Response({
                        "display": name
                    })
                elif name in file:
                    possible_files.append(file)
            if possible_files:
                return Response({
                    "entries": possible_files
                })
            else:
                return Response({
                    "page_exists": False
                })
        # Response to URLs w/o query parameters
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
                "content": content
            })
        return Response({})
    elif request.method == "PUT":
        title = request.data["title"].lower()
        content = request.data["content"]
        util.save_entry(title, content)
        return Response({
            "file_updated": True
        })
