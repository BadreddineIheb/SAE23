from django.db import models

# Create your models here.

# model de étudiant

class Etudiant(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    groupe = models.CharField(max_length=25)
    photo = models.ImageField(blank=False)
    email = models.EmailField(max_length=100)
    # num_etud = models.ForeignKey("continent", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Lors de l'examen {self.examen} l'étudiant {self.etudiant} a eu la note de {self.note} avec un coefficient de {self.coefficient}"
        return chaine

    def dico(self):
        return {"examen":self.examen, "etudiant":self.etudiant, "note":self.note, "coefficient":self.coefficient} #"continent":self.continent}






# model de Notes

class Notes(models.Model):
    examen = models.CharField(max_length=100)
    etudiant = models.CharField(max_length=100)
    note = models.FloatField(blank=False)
    coefficient = models.FloatField(blank=False)
    #continent= models.ForeignKey("continent", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Lors de l'examen {self.examen} l'étudiant {self.etudiant} a eu la note de {self.note} avec un coefficient de {self.coefficient}"
        return chaine

    def dico(self):
        return {"examen":self.examen, "etudiant":self.etudiant, "note":self.note, "coefficient":self.coefficient} #"continent":self.continent}


# model des ressources
class Ressource(models.Model):
  #  ressource_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    descriptif = models.TextField()
    coefficient = models.FloatField()

    def __str__(self):
        return self.nom


