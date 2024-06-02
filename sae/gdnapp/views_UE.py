from django.shortcuts import render, HttpResponseRedirect
from .forms import UEForm
from .import models


def index(request):
    liste = list(models.UE.objects.all())
    return render(request, "UE/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = UEForm(request)
        return render(request, "UE/ajout.html", {"form":form })
    else:
        form = UEForm()
        return render(request, "UE/ajout.html", {"form": form})

def update(request, id):
    ue = models.UE.objects.get(pk=id)
    form = UEForm(ue.dico())
    return render(request, "UE/update.html", {"form": form, "id": id})

def delete(request, id):
    ue = models.UE.objects.get(pk=id)
    ue.delete()
    return HttpResponseRedirect("/gdnapp/UE/index/")


def traitement(request):
    qform = UEForm(request.POST)
    if qform.is_valid():
        ue= qform.save()
        return HttpResponseRedirect("/gdnapp/UE/index/")
    else:
        return render(request,"UE/ajout.html",{"form":qform})

def updatetraitement(request,id):
    qform = UEForm(request.POST)
    if qform.is_valid():
        ue = qform.save(commit=False)
        ue.id = id
        ue.save()
        return HttpResponseRedirect("/gdnapp/UE/index/")
    else:
        return render(request,"UE/ajout.html",{"form":qform,"id": id})