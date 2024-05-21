from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

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