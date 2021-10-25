from django.shortcuts import render
from . import util
from markdown2 import markdown
import re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def content(request, name):
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


def search(request):
    title = request.GET['q']
    if util.get_entry(title) is None:
        slist = util.list_entries()
        entries = [x for x in slist if title in x]
        return render(request, "encyclopedia/search.html", {
            "entries": entries,
            "stri": title
        })
    else:
        mark = util.get_entry(title)
        return render(request, "encyclopedia/content.html", {
            "name": title,
            "content": markdown(mark)
        })
