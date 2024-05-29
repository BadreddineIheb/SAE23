from django.shortcuts import render, get_object_or_404, redirect
from .models import Enseignant
from .forms import EnseignantForm



def enseignant_list(request):
    if request.method == 'POST' and 'enseignant_id' in request.POST:
        enseignant = get_object_or_404(Enseignant, id=request.POST.get('enseignant_id'))
        enseignant.delete()
        return render(request, 'enseignant/enseignant_list.html', {'enseignant': enseignant})

    enseignants = Enseignant.objects.all()
    return render(request, 'enseignant/enseignant_list.html', {'enseignants': enseignants})


def enseignant_create_or_update(request, id=None):
    if id:
        enseignant = get_object_or_404(Enseignant)
    else:
        enseignant = None

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return render(request, 'enseignant/enseignant_affichage.html', {'enseignant': enseignant})

    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'enseignant/enseignant_affichage.html', {'form': form, 'enseignant': enseignant})


def enseignant_affichage(request):

    return render(request, 'enseignant/enseignant_affichage.html', {'enseignant': enseignant})
