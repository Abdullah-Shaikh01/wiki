from django.shortcuts import render


def content(request, name):
    return render(request, "wiki/index.html", {
        "name": name
    })
