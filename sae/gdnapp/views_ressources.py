from django.shortcuts import render, HttpResponseRedirect
from .forms import RessourcesForm
from .models import Ressources

def index(request):
    liste = list(Ressources.objects.all())
    return render(request, "ressources/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = RessourcesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/gdnapp/ressources/index/")
    else:
        form = RessourcesForm()
    return render(request, "ressources/ajout.html", {"form": form})

def update(request, id):
    ressource = Ressources.objects.get(pk=id)
    form = RessourcesForm(instance=ressource)
    return render(request, "ressources/update.html", {"form": form, "id": id})

def delete(request, id):
    ressource = Ressources.objects.get(pk=id)
    ressource.delete()
    return HttpResponseRedirect("/gdnapp/ressources/index/")

def traitement(request):
    if request.method == "POST":
        form = RessourcesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/gdnapp/ressources/index/")
    else:
        form = RessourcesForm()
    return render(request, "ressources/ajout.html", {"form": form})

def updatetraitement(request, id):
    ressource = Ressources.objects.get(pk=id)
    form = RessourcesForm(request.POST, instance=ressource)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/gdnapp/ressources/index/")
    return render(request, "ressources/update.html", {"form": form, "id": id})
