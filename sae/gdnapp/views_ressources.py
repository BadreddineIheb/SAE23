from django.shortcuts import render, get_object_or_404

from .forms import RessourceForm
from .models import Ressource


def ressource_list(request):
    if request.method == 'POST':
        ressource = get_object_or_404(Ressource, id=request.POST.get('ressource_id'))
        ressource.delete()
        return render(request, 'ressource/ressource_form.html', {'ressource': ressource})

    ressources = Ressource.objects.all()
    return render(request, 'ressource/ressource_list.html', {'ressources': ressources})


def ressource_create(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ressource/ressource_list.html', {'form': form})
    else:
        form = RessourceForm()

    return render(request, 'ressource/ressource_form.html', {'form': form})


def ressource_update(request, id):
    ressource = get_object_or_404(Ressource, id=id)
    if request.method == 'POST':
        form = RessourceForm(request.POST, instance=ressource)
        if form.is_valid():
            form.save()
            return render(request, 'ressource/ressource_list.html', {'form': form})
    else:
        form = RessourceForm(instance=ressource)
    return render(request, 'ressource/ressource_form.html', {'form': form})


def ressource_affichage(request, pk):
    ressource = get_object_or_404(Ressource, pk=pk)
    return render(request, 'ressource/ressource_affichage.html', {'ressource': ressource})
