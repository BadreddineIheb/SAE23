from django.shortcuts import render, HttpResponseRedirect
from .forms import NotesForm
from .import models


def index(request):
    liste = list(models.Notes.objects.all())
    return render(request, "notes/index.html", {"liste": liste})

def ajout(request):
    if request.method =="POST":
        form = NotesForm(request)
        return render(request, "notes/ajout.html", {"form":form})
    else:
        form = NotesForm()
        return render(request, "notes/ajout.html", {"form": form})

def update(request, id):
    notes = models.Notes.objects.get(pk=id)
    form = NotesForm(notes.dico())
    return render(request, "notes/update.html", {"form": form, "id": id})

def delete(request, id):
    notes = models.Notes.objects.get(pk=id)
    notes.delete()
    return HttpResponseRedirect("/gdnapp/index/")


def traitement(request):
    nform = NotesForm(request.POST)
    if nform.is_valid():
        notes = nform.save()
        return render(request, 'notes/index.html', {'notes' : notes})
    else:
        return render(request,"notes/ajout.html",{"form":nform})

def updatetraitement(request,id):
    nform = NotesForm(request.POST)
    if nform.is_valid():
        notes = nform.save(commit=False)
        notes.id = id
        notes.save()
        return HttpResponseRedirect("/gdnapp/index/")
    else:
        return render(request,"notes/ajout.html",{"form":nform,"id": id})



