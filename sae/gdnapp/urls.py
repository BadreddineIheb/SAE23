from django.urls import path

from . import views_enseignants, views_UE, views_ressources, views_etudiant, views_notes, views_examen,views_accueil

urlpatterns = [
    path('', views_accueil.index),
    path('etudiant/index/', views_etudiant.index),
    path('etudiant/ajout/', views_etudiant.ajout),
    path('etudiant/update/<int:id>/', views_etudiant.update),
    path('etudiant/delete/<int:id>/', views_etudiant.delete),
    path('etudiant/updatetraitement/<int:id>/', views_etudiant.updatetraitement),
    path('etudiant/traitement/', views_etudiant.traitement),


    path('UE/index/', views_UE.index),
    path('UE/ajout/', views_UE.ajout),
    path('UE/update/<int:id>/', views_UE.update),
    path('UE/delete/<int:id>/', views_UE.delete),
    path('UE/updatetraitement/<int:id>/', views_UE.updatetraitement),
    path('UE/traitement/', views_UE.traitement),

    path('notes/index/', views_notes.index),
    path('notes/ajout/', views_notes.ajout),
    path('notes/update/<int:id>/', views_notes.update),
    path('notes/delete/<int:id>/', views_notes.delete),
    path('notes/updatetraitement/<int:id>/', views_notes.updatetraitement),
    path('notes/traitement/', views_notes.traitement),

    path('examen/index/', views_examen.index),
    path('examen/ajout/', views_examen.ajout),
    path('examen/update/<int:id>/', views_examen.update),
    path('examen/delete/<int:id>/', views_examen.delete),
    path('examen/updatetraitement/<int:id>/', views_examen.updatetraitement),
    path('examen/traitement/', views_examen.traitement),

    path('ressource/index/', views_ressources.index),
    path('ressource/ajout/', views_ressources.ajout),
    path('ressource/update/<int:id>/', views_ressources.update),
    path('ressource/delete/<int:id>/', views_ressources.delete),
    path('ressource/traitement/', views_ressources.traitement),
    path('ressource/updatetraitement/<int:id>/', views_ressources.updatetraitement),

    path('enseignant/index/', views_enseignants.index),
    path('enseignant/ajout/', views_enseignants.ajout),
    path('enseignant/update/<int:id>/', views_enseignants.update),
    path('enseignant/delete/<int:id>/', views_enseignants.delete),
    path('enseignant/traitement/', views_enseignants.traitement),
    path('enseignant/updatetraitement/<int:id>/', views_enseignants.updatetraitement),
]
