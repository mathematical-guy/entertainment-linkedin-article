from django.contrib import admin

from .models import Anime, Character


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'has_watched')
    list_filter = ('has_watched',)
    search_fields = ('name',)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'belongs_to')
    list_filter = ('belongs_to',)
    search_fields = ('name',)
