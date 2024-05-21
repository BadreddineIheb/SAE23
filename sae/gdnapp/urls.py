from django.urls import path

from . import views_enseignants, views_UE, views_ressources, views_etudiant, views_notes, views_examens

urlpatterns = [
    path('index/', views_notes.index),
]
