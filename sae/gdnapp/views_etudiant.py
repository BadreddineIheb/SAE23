from django.shortcuts import render, HttpResponseRedirect
from .forms import EtudiantForm, UploadFileForm
from .import models
import csv
from io import TextIOWrapper


def index(request):
    liste = list(models.Etudiant.objects.all())
    return render(request, "etudiant/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "netudiant/ajout.html", {"form":form})
        else:
            print(form.errors)
    else:
        form = EtudiantForm()
        return render(request, "etudiant/ajout.html", {"form": form})

def update(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(request.POST or None, request.FILES or None, instance=etudiant)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/gdnapp/etudiant/index/")
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

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['fichier']
            decoded_file = TextIOWrapper(file.file, encoding='utf-8')
            reader = csv.reader(decoded_file)
            next(reader)  # skip header row if there is one
            for row in reader:
                nom, prenom, groupe, email = row[0], row[1], row[2], row[3] if len(row) > 3 else ''
                models.Etudiant.objects.create(nom=nom, prenom=prenom, groupe=groupe, email=email)
            return HttpResponseRedirect("/gdnapp/etudiant/index/")
    else:
        form = UploadFileForm()
    return render(request, 'etudiant/upload.html', {'form': form})