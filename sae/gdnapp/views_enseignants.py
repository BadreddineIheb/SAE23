from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantsForm
from .import models


def index(request):
    liste = list(models.Enseignants.objects.all())
    return render(request, "enseignant/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = EnseignantsForm(request)
        return render(request, "enseignant/ajout.html", {"form":form })
    else:
        form = EnseignantsForm()
        return render(request, "enseignant/ajout.html", {"form": form})

def update(request, id):
    enseignant = models.Enseignants.objects.get(pk=id)
    form = EnseignantsForm(enseignant.dico())
    return render(request, "enseignant/update.html", {"form": form, "id": id})

def delete(request, id):
    enseignant = models.Enseignants.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/gdnapp/enseignant/index/")


def traitement(request):
    eform = EnseignantsForm(request.POST)
    if eform.is_valid():
        enseignant= eform.save()
        return HttpResponseRedirect("/gdnapp/enseignant/index/")
    else:
        return render(request,"enseignant/ajout.html",{"form":eform})

def updatetraitement(request,id):
    eform = EnseignantsForm(request.POST)
    if eform.is_valid():
        enseignant = eform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/gdnapp/enseignant/index/")
    else:
        return render(request,"enseignant/ajout.html",{"form":eform,"id": id})