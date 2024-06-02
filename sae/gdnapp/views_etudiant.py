from django.shortcuts import render, HttpResponseRedirect
from .forms import EtudiantForm
from .import models


def index(request):
    liste = list(models.Etudiant.objects.all())
    return render(request, "etudiant/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = EtudiantForm(request)
        return render(request, "netudiant/ajout.html", {"form":form})
    else:
        form = EtudiantForm()
        return render(request, "etudiant/ajout.html", {"form": form})

def update(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(etudiant.dico())
    return render(request, "etudiant/update.html", {"form": form, "id": id})

def delete(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/gdnapp/etudiant/index/")


def traitement(request):
    wform = EtudiantForm(request.POST)
    if wform.is_valid():
        etudiant= wform.save()
        return HttpResponseRedirect("/gdnapp/etudiant/index/")
    else:
        return render(request,"etudiant/ajout.html",{"form":wform})

def updatetraitement(request,id):
    wform = EtudiantForm(request.POST)
    if wform.is_valid():
        etudiant = wform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/gdnapp/etudiant/index/")
    else:
        return render(request,"etudiant/ajout.html",{"form":wform,"id": id})