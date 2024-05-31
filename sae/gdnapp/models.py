from django.db import models

# Create your models here.

# model de étudiant

class Etudiant(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    groupe = models.CharField(max_length=25)
    photo = models.ImageField(blank=True)
    email = models.EmailField(max_length=100)
    # num_etud = models.ForeignKey("etudiant", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"L'étudiant {self.nom} {self.prenom} fait partie des {self.groupe}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom, "groupe":self.groupe}

class UE(models.Model) :
    nom = models.CharField(max_length=30)
    semestre = models.IntegerField(null=False, blank=False)
    credit = models.IntegerField(null=True, blank=True)
    # code = models.ForeignKey("UE", on-delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"L'unité d'enseignement {self.nom} présente au {self.semestre} semestre donne {self.credit} crédits ECTS"
        return chaine

    def dico(self):
        return {"nom": self.nom, "semestre": self.semestre, "credit": self.credit}


# model de Notes

class Notes(models.Model):
    examen = models.CharField(max_length=100)
    etudiant = models.CharField(max_length=100)
    note = models.FloatField(blank=False)
    appreciation = models.TextField(null=True, blank=True)
    #continent= models.ForeignKey("continent", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Lors de l'examen {self.examen} l'étudiant {self.etudiant} a eu la note de {self.note} avec l'appréciation : {self.appreciation}"
        return chaine

    def dico(self):
        return {"examen":self.examen, "etudiant":self.etudiant, "note":self.note, "appreciation":self.appreciation} #"continent":self.continent}


# model des ressources
class Ressources(models.Model):
    code_ressource = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null=True, blank=True)
    coefficient = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.code_ressource} - {self.nom}"



class Enseignants(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# model de examen

class Examen(models.Model):
    id_examen = models.IntegerField(blank=False)
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    coefficient = models.FloatField(blank=False)
    #continent= models.ForeignKey("continent", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"L'examen avec l'id {self.id_examen} et avec le titre {self.titre} en date de  {self.date} a un coefficient de {self.coefficient}"
        return chaine

    def dico(self):
        return {"id":self.id_examen, "titre":self.titre, "date":self.date, "coefficient":self.coefficient} #"continent":self.continent}
