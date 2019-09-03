from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FilmForm, CommentaireForm, AvisForm
from .models import Films, Avis, Commentaires
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

# Create your views here.

def acceuil_view(request):
    film_obj = Films.objects.all()
    nombre_film = Films.objects.all().count()
    form_view_film = FilmForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form_view_film.is_valid():
            # form_view_film.save()
            currentuser = request.user
            titre = form_view_film.cleaned_data['titre']
            acteur = form_view_film.cleaned_data['acteur']
            description = form_view_film.cleaned_data['description']
            language = form_view_film.cleaned_data['language']
            resolution = form_view_film.cleaned_data['resolution']
            cover = form_view_film.cleaned_data['cover']
            film = form_view_film.cleaned_data['film']

            Films(user = currentuser,titre = titre,acteur = acteur,description = description,language = language,resolution = resolution,cover = cover,film = film).save()
            nombre_film = Films.objects.all().count()
            msg = "Enregistrer avec success !!!"
    return render( request, 'acceuil.html',locals() )

def profil_view(request,slug):
    film_obj = Films.objects.get( slug = slug )
    comm_obj = Commentaires.objects.filter( titre = film_obj )
    all_likes = Avis.objects.filter(Q(likes="1")).count()
    all_dislikes = Avis.objects.filter(Q(dislikes="1")).count()
    
    form_view_comm = CommentaireForm(request.POST or None)
    if request.method == "POST":
        if form_view_comm.is_valid():
            current_user = request.user
            # titr = form_view_comm.cleaned_data['titre']
            com = form_view_comm.cleaned_data['commentaire']
            Commentaires(user = current_user,titre = film_obj,commentaire = com).save()
            msg = "Enregistrer avec success !!!"

    form_view_avi = AvisForm(request.POST or None)
    if request.method == "POST":
        if form_view_avi.is_valid():
            current_user = request.user
            film_key = str(current_user)+str(slug)
            Avis( user = current_user, slug_key = film_key, likes = 1 ).save()
            all_likes = Avis.objects.filter(Q(likes="1") & Q(slug_key=film_obj)).count()
            all_dislikes = Avis.objects.filter(Q(dislikes="1") & Q(slug_key=film_obj)).count()
            mssg = "Liked!!!"

    form_view_avi1 = AvisForm(request.POST or None)
    if request.method == "POST":
        if form_view_avi1.is_valid():
            current_user1 = request.user
            film_key1 = str(current_user1)+str(slug)
            Avis( user = current_user1, slug_key = film_key, dislikes = 1 ).save()
            all_likes = Avis.objects.filter(likes="1").count()
            all_dislikes = Avis.objects.filter(dislikes="1").count()
            mssg1 = "Disliked!!!"
            
    return render( request, 'profil.html',locals() )




