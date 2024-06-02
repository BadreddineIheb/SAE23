from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EtudiantForm(ModelForm):
    class Meta :
        model = models.Etudiant
        fields = ('nom', 'prenom', 'groupe', 'photo', 'email')
        labels = {
            'nom' : _('Nom de l\'étudiant'),
            'prenom' : _('Prénom de l\'étudiant'),
            'groupe' : _('Groupe auquel appartient l\'étudiant'),
            'photo' : _('Photo de l\'étudiant'),
            'email' : _('Adresse mail de l\'étudiant'),
        }

class UEForm(ModelForm):
    class Meta:
        model = models.UE
        fields = ('code','nom', 'semestre', 'credit')
        labels = {
            'code': _('Code '),
            'nom' : _('Nom de l\'unité d\'enseignement'),
            'semestre' : _('Semestre dans lequel cette UE est présente'),
            'credit' : _('Crédit ECTS que donne cet UE'),
        }

class NotesForm(ModelForm):
    class Meta :
        model = models.Notes
        fields = ('examen', 'etudiant', 'note', 'appreciation')
        labels = {
            'examen': _('Examen'),
            'etudiant': _('Etudiant'),
            'note': _('Note'),
            'appreciation': _('Appréciation')
        }

class ExamenForm(ModelForm):
    class Meta :
        model = models.Examen
        fields = ( 'enseignant','titre', 'date', 'coefficient')
        labels = {
            'enseignant': _('Enseignant'),
            'titre': _('titre'),
            'date': _('date'),
            'coefficient': _('Coefficient')
        }

class RessourcesForm(ModelForm):
    class Meta:
        model = models.Ressources
        fields = ('code_ressource', 'nom', 'descriptif', 'coefficient')

class EnseignantsForm(ModelForm):
    class Meta:
        model = models.Enseignants
        fields = ('id_examen','nom', 'prenom')
        labels = {
            'id_examen': _('id'),
            'nom': 'Nom',
            'prenom': 'Prénom'
        }
