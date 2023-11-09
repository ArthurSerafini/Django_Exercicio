from django.shortcuts import render

from . import util

from django import forms

class NewSearchForm(forms.Form):
    search = forms.CharField(label="new search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    return render(request, "encyclopedia/title.html", {
        "name": name,
        "entries": util.list_entries(),
        "md_page": util.get_entry(name)
    })

def search(request):
    return render(request, "encyclopedia/index.html", {
        "form": NewSearchForm()
    })

