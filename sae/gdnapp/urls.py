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


    path('ressource/affichage/', views_ressources.ressource_affichage),
    path('ressource/', views_ressources.ressource_list),
    path('ressource/create/', views_ressources.ressource_create),
    path('ressource/<int:id>/edit/', views_ressources.ressource_update),





    path('enseignants/affichage', views_enseignants.enseignant_affichage),
    path('enseignants/create/', views_enseignants.enseignant_create_or_update),
    path('enseignants/<int:id>/edit/', views_enseignants.enseignant_create_or_update),
    path('enseignants/<int:id>/', views_enseignants.enseignant_affichage),
]
