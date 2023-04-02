from django.db.models import F
from django.shortcuts import render
from . import models


# Todo: make endpoints for detail views

def anime_list(request):
    anime = list(models.Anime.objects.values())
    context = {"animes": anime}

    return render(request=request, template_name="anime-list.html", context=context)


def character_list(request):
    characters = list(
        models.Character.objects.annotate(
            anime=F('belongs_to__name')
        ).values()
    )
    context = {"characters": characters}
    return render(request=request, template_name="character-list.html", context=context)

