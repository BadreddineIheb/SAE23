from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import NotesForm,Fichiernotes
from .import models
import csv
from io import TextIOWrapper

def releve_notes(request, etudiant_id):
    etudiant = get_object_or_404(models.Etudiant, pk=etudiant_id)
    notes = models.Notes.objects.filter(etudiant=etudiant)
    return render(request, 'notes/releve_notes.html', {'etudiant': etudiant, 'notes': notes})

def index(request):
    liste = list(models.Notes.objects.all())
    return render(request, "notes/index.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = NotesForm(request)
        return render(request, "notes/ajout.html", {"form":form })
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
    return HttpResponseRedirect("/gdnapp/notes/index/")


def traitement(request):
    nform = NotesForm(request.POST)
    if nform.is_valid():
        notes= nform.save()
        return HttpResponseRedirect("/gdnapp/notes/index/")
    else:
        return render(request,"notes/ajout.html",{"form":nform})

def updatetraitement(request,id):
    nform = NotesForm(request.POST)
    if nform.is_valid():
        notes = nform.save(commit=False)
        notes.id = id
        notes.save()
        return HttpResponseRedirect("/gdnapp/notes/index/")
    else:
        return render(request,"notes/ajout.html",{"form":nform,"id": id})

def upload_file(request):
    if request.method == 'POST':
        form = models.Fichiernotes(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['fichiernotes']
            decoded_file = TextIOWrapper(file.file, encoding='utf-8')
            reader = csv.reader(decoded_file)
            next(reader)
            for row in reader:
                if len(row) == 10:
                    examen_id_exam, examen_titre, examen_date, examen_coefficient, etudiant_nom, etudiant_prenom, etudiant_groupe, etudiant_email, note, appreciation = row
                    examen, created = models.Examen.objects.get_or_create(id_exam=examen_id_exam,titre=examen_titre, date=examen_date,coefficient=examen_coefficient)
                    etudiant, created = models.Etudiant.objects.get_or_create(nom=etudiant_nom, prenom=etudiant_prenom,groupe=etudiant_groupe,email=etudiant_email)
                    models.Notes.objects.create(examen=examen, etudiant=etudiant, note=note, appreciation=appreciation)
                else:
                    print("Erreur: La ligne ne contient pas le bon nombre de valeurs")
            return HttpResponseRedirect("/gdnapp/notes/index/")

    else:
        form = Fichiernotes()
    return render(request, 'notes/upload.html', {'form': form})



