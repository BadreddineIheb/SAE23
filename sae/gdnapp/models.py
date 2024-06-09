from django.db import models
from django import forms

# Create your models here.
class Fichiernotes(forms.Form):
    fichiernotes = forms.FileField()

class UploadFileForm(forms.Form):
    fichier = forms.FileField()
# model de étudiant

class Etudiant(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    groupe = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='photo/', blank=True)
    email = models.EmailField(max_length=100, blank=True)
    # num_etud = models.ForeignKey("etudiant", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"L'étudiant {self.nom} {self.prenom} du groupe {self.groupe} avec l'email {self.email}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom, "groupe":self.groupe}

class UE(models.Model) :
    code = models.IntegerField(null=False, blank = True)
    nom = models.CharField(max_length=30)
    semestre = models.IntegerField(null=False, blank=False)
    credit = models.IntegerField(null=True, blank=True)
    # code = models.ForeignKey("UE", on-delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"L'unité d'enseignement {self.code} {self.nom} présente au {self.semestre} semestre donne {self.credit} crédits ECTS"
        return chaine

    def dico(self):
        return {"code":self.code,"nom": self.nom, "semestre": self.semestre, "credit": self.credit}


# model de Notes

class Notes(models.Model):
    etudiant = models.ForeignKey("etudiant", on_delete=models.CASCADE, default=None)
    #etudiant=models.CharField(max_length=100)
    note = models.FloatField(blank=False)
    appreciation = models.TextField(null=True, blank=True)
    examen = models.ForeignKey("examen", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Lors de {self.examen}. {self.etudiant} a eu la note de {self.note} avec l'appréciation : {self.appreciation}"
        return chaine

    def dico(self):
        return {"examen":self.examen, "etudiant":self.etudiant, "note":self.note, "appreciation":self.appreciation}


# model des ressources
class Ressources(models.Model):
    UE = models.ForeignKey("ue", on_delete=models.CASCADE, default=None, blank=True)
    code_ressource = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null=True, blank=True)
    coefficient = models.FloatField(blank=False)

    def __str__(self):
        return f" Dans {self.UE} il y a {self.code_ressource} - {self.nom} a un coefficient de {self.coefficient}. La description est {self.descriptif}"

    def dico(self):
        return {"UE":self.UE,"code_ressource":self.code_ressource,"nom": self.nom, "descriptif": self.descriptif, "coefficient": self.coefficient}


class Enseignants(models.Model):
    id_examen = models.IntegerField(null=False, blank=True)
    nom = models.CharField(max_length=100, blank =True)
    prenom = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"professeur {self.nom} {self.prenom}"

    def dico(self):
        return {"id":self.id_examen, "nom":self.prenom, "date":self.prenom}
# model de examen

class Examen(models.Model):
    id_exam =models.IntegerField(blank=True)
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    coefficient = models.FloatField(blank=False)

    def __str__(self):
        chaine = f"L'examen n°{self.id_exam} qui s'intitule {self.titre} en date de  {self.date} avec un coefficient de {self.coefficient}"
        return chaine

    def dico(self):
        return {"id":self.id_exam, "titre":self.titre, "date":self.date, "coefficient":self.coefficient} #"continent":self.continent}
