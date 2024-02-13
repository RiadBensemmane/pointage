from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='employe-list'),
    path('detail/<str:pk>/', views.detail, name='employe-detail'),
    path('update_sheet/<str:pk>/', views.updateSheet, name='sheet-update'),
    path('ajouter/', views.ajouter_employe, name='employe-ajout'),
    path('update/<str:pk>/', views.update_employe, name='employe-update'),
    path('download/', views.download, name='download'),
]
