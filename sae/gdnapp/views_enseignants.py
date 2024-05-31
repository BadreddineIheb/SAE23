from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantsForm
from .models import Enseignants

def index(request):
    liste = list(Enseignants.objects.all())
    return render(request, "enseignants/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = EnseignantsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/gdnapp/enseignants/index/")
        return render(request, "enseignants/ajout.html", {"form": form})
    else:
        form = EnseignantsForm()
        return render(request, "enseignants/ajout.html", {"form": form})

def update(request, id):
    item = Enseignants.objects.get(pk=id)
    form = EnseignantsForm(instance=item)
    return render(request, "enseignants/update.html", {"form": form, "id": id})

def delete(request, id):
    item = Enseignants.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect("/gdnapp/enseignants/index/")

def traitement(request):
    form = EnseignantsForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/gdnapp/enseignants/index/")
    return render(request, "enseignants/ajout.html", {"form": form})

def updatetraitement(request, id):
    item = Enseignants.objects.get(pk=id)
    form = EnseignantsForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/gdnapp/enseignants/index/")
    return render(request, "enseignants/update.html", {"form": form, "id": id})
