from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=64, unique=True)
    has_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=64, unique=True)
    belongs_to = models.ForeignKey(Anime, related_name="characters", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.belongs_to.name} - {self.name}"



