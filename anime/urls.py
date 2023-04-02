from django.urls import path
from . import views


urlpatterns = [
    path('anime_list/', views.anime_list),
    path('character_list/', views.character_list),
]

