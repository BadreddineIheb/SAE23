from django.shortcuts import render, HttpResponseRedirect
from .forms import NotesForm
from .import models


def index(request):
    liste = list(models.Notes.objects.all())
    return render(request, "pays/index.html", {"liste": liste})
