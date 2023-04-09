from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return f"Актер - {self.name}"


class Movie(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    actors = models.ManyToManyField(to=Actor, verbose_name="Актеры")
    year = models.IntegerField(verbose_name="Год")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return f"Фильм - {self.title}"
