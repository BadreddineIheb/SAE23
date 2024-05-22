from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EtudForm(ModelForm):
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


class NotesForm(ModelForm):
    class Meta :
        model = models.Notes
        fields = ('examen', 'etudiant', 'note', 'coefficient')
        labels = {
            'examen': _('Examen'),
            'etudiant': _('Etudiant'),
            'note': _('Note'),
            'coefficient': _('Coefficient')
        }

class RessourceForm(ModelForm):
    class Meta:
        model = models.Ressource
        fields = ('nom', 'descriptif', 'coefficient')
