from django.shortcuts import render, HttpResponseRedirect
from .forms import EtudForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = EtudForm(request)
        return render(request, 'etudiant/ajout.html', {'form': form})
    else :
        form = EtudForm()
        return render(request, 'etudiant/ajout.html', {'form' : form})

def affichage(request):
    lform = EtudForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save()
        return render(request, 'etudiant/affichage.html', {'etudiant' : etudiant})
    else :
        return render(request, 'etudiant/ajout.html', {'form' : lform})

"""
def update(request, id):
    etudiant = models.etudiant.objects.get(pk = id)
    form = EtudForm(etudiant.dico())
    return render(request,"etudiant/ajout.html",{"form": form, 'id':id})

def updateaffichage(request, id):
    Eform = EtudForm(request.POST)
    if Eform.is_valid():
        etudiant = Eform.save(commit = False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("etudiant/affichage.html")
    else:
        return render(request, "etudiant/ajout.html", {'form' : Eform, 'id': id})

def delete(request, id):
    etudiant = models.etudiant.objects.get(pk = id)
    etudiant.delete()
    return HttpResponseRedirect("etudiant/affichage.html")
"""