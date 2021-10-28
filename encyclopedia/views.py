from django.shortcuts import render
from . import util
from markdown2 import markdown
import re
from django import forms
from django.shortcuts import HttpResponse, reverse
import random


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


class NewPageForm(forms.Form):
    title = forms.CharField(label="Topic name")
    content = forms.CharField(widget=forms.Textarea, help_text="Please use markdown language")


def add_page(request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewPageForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the title and content from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            if util.get_entry(title):
                return HttpResponse("<h1> Sorry, the page with same name already exists</h1>")
            contents = form.cleaned_data["content"]

            # Add the new task to our list of tasks
            util.save_entry(title, contents)
            # Redirect user to list of tasks
            return content(request, title)

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/addPage.html", {
                "form": NewPageForm()
            })
    return render(request, "encyclopedia/addPage.html", {
        "form": NewPageForm()
    })


def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        return render(request, "encyclopedia/EditPage.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    return render(request, "encyclopedia/addPage.html", {
        "form": NewPageForm()
    })


def save(request):
    if request.method == "POST":
        title = request.POST['newtitle']
        contents = request.POST['newcontent']
        util.save_entry(title, contents)
        return content(request, title)


def randomPage(request):
    return content(request, random.choice(util.list_entries()))
