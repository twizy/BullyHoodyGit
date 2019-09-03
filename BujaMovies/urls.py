from django.urls import path
from . import views

urlpatterns = [
    path( '', views.acceuil_view, name="acc" ),
    path( 'profil/<slug>/', views.profil_view, name="profil" ),
]