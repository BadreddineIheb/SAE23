from django.urls import path

from . import views_enseignants, views_UE, views_ressources, views_etudiant, views_notes, views_examens

urlpatterns = [
    path('etudiant/ajout/', views_etudiant.ajout),
    path('etudiant/affichage/', views_etudiant.affichage),






    path('notes/index/', views_notes.index),
    path('notes/ajout/', views_notes.ajout),
    path('updatenotes/<int:id>/', views_notes.update),
    path('deletenotes/<int:id>/', views_notes.delete),
    path('updatetraitementnotes/<int:id>/', views_notes.updatetraitement),
    path('notes/traitement/', views_notes.traitement),


    path('ressource/affichage/', views_ressources.ressource_affichage),
    path('ressource/', views_ressources.ressource_list),
    path('ressource/create/', views_ressources.ressource_create),
    path('ressource/<int:id>/edit/', views_ressources.ressource_update),
]
