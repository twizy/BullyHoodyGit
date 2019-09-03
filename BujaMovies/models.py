from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Films(models.Model):
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    titre = models.CharField( verbose_name  = "Titre", null=False, max_length = 30 )
    acteur = models.CharField( verbose_name = "Acteur principale", null=False, max_length = 25)
    description = models.TextField( verbose_name = "Description", null=False )
    language = models.CharField( verbose_name = "Language", null = True, default = "lang", max_length = 3 )
    resolution = models.IntegerField( verbose_name = "Resolution" )
    date = models.DateTimeField( default = timezone.now )
    slug = models.SlugField(unique=True, max_length=100, null = True)
    cover = models.ImageField( upload_to = 'Covers/', null = True, blank = True )
    film = models.FileField( upload_to = 'Videos/', null = True, blank = True )

    def save(self,*args,**kwargs):
        self.slug = slugify(self.titre[:30]+str(self.date))#to compare if the we found identical values
        super(Films, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.titre}"
        # {self.resolution} {self.acteur} {self.language} {self.description} {self.date}

class Commentaires(models.Model):
    user = models.ForeignKey ( User, on_delete = models.CASCADE )
    titre = models.ForeignKey( Films, verbose_name = "Choisir Titre", on_delete = models.CASCADE )
    commentaire = models.TextField ( verbose_name = "Commenter",null=False )
    date = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return f"{self.user} made this comment {self.commentaire}"


class Avis(models.Model):
    user = models.ForeignKey ( User, on_delete = models.CASCADE )
    slug_key = models.CharField(max_length=50, verbose_name = "Slug key")
    likes = models.IntegerField ( default = 0 )
    dislikes = models.IntegerField ( default = 0 )

    def __str__(self):
        return f"{self.slug_key} ~ likes: {self.likes} ~dislikes: {self.dislikes}"
