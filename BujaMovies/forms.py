from django import forms
from .models import *

class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ('titre','acteur','description','language','resolution','cover','film')

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        fields = ('commentaire',)

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        exclude = ('user','likes','dislikes','slug_key',)
