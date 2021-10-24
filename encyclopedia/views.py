from django.shortcuts import render
from . import util
from markdown2 import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def content(request, name):
    # return render(request, "wiki/index.html", {
    #     "name": name
    # })
    if util.get_entry(name):
        mark = util.get_entry(name)
        return render(request, "encyclopedia/content.html", {
            "name": name,
            "content": markdown(mark)
        })
    else:
        return render(request, "encyclopedia/not_found.html", {
            "name": name
        })

