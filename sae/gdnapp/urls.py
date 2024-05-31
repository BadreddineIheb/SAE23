from django.urls import path

from . import views_enseignants, views_UE, views_ressources, views_etudiant, views_notes, views_examen

urlpatterns = [
    path('etudiant/ajout/', views_etudiant.ajout),
    path('etudiant/affichage/', views_etudiant.affichage),






    path('notes/index/', views_notes.index),
    path('notes/ajout/', views_notes.ajout),
    path('notes/update/', views_notes.update),
    path('notes/delete/', views_notes.delete),
    path('notes/updatetraitement/', views_notes.updatetraitement),
    path('notes/traitement/', views_notes.traitement),

    path('examen/index/', views_examen.index),
    path('examen/ajout/', views_examen.ajout),
    path('examen/update/', views_examen.update),
    path('examen/delete/', views_examen.delete),
    path('examen/updatetraitement/', views_examen.updatetraitement),
    path('examen/traitement/', views_examen.traitement),

    path('ressources/index/', views_ressources.index),
    path('ressources/ajout/', views_ressources.ajout),
    path('ressources/update/', views_ressources.update),
    path('ressources/delete/', views_ressources.delete),
    path('ressources/traitement/', views_ressources.traitement),
    path('ressources/updatetraitement/', views_ressources.updatetraitement),

    path('enseignants/index/', views_enseignants.index),
    path('enseignants/ajout/', views_enseignants.ajout),
    path('enseignants/update/', views_enseignants.update),
    path('enseignants/delete/', views_enseignants.delete),
    path('enseignants/traitement/', views_enseignants.traitement),
    path('enseignants/updatetraitement/', views_enseignants.updatetraitement),
]
