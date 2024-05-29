from django.shortcuts import render, HttpResponseRedirect
from .forms import ExamenForm
from .import models


def index(request):
    liste = list(models.Examen.objects.all())
    return render(request, "examen/index.html", {"liste": liste})

def ajout(request):
    if request.method =="POST":
        form = ExamenForm(request)
        return render(request, "examen/ajout.html", {"form":form})
    else:
        form = ExamenForm()
        return render(request, "examen/ajout.html", {"form": form})

def update(request, id):
    notes = models.Examen.objects.get(pk=id)
    form = ExamenForm(notes.dico())
    return render(request, "examen/update.html", {"form": form, "id": id})

def delete(request, id):
    notes = models.Examen.objects.get(pk=id)
    notes.delete()
    return HttpResponseRedirect("/gdnapp/index/")


def traitement(request):
    nform = ExamenForm(request.POST)
    if nform.is_valid():
        examen = nform.save()
        return render(request, 'examen/index.html', {'examen' : examen})
    else:
        return render(request,"examen/ajout.html",{"form":nform})

def updatetraitement(request,id):
    nform = ExamenForm(request.POST)
    if nform.is_valid():
        examen = nform.save(commit=False)
        examen.id = id
        examen.save()
        return HttpResponseRedirect("/gdnapp/index/")
    else:
        return render(request,"examen/ajout.html",{"form":nform,"id": id})


