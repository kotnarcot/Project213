from django.db import models


class Task(models.Model):
     title = models.CharField('Название', max_length=50)
     task = models.TextField('Описание')

     def __str__(self):
         return self.title

class Country (models.Model):
    name = models.CharField('Название страны', max_length=20)
    population = models.CharField('Население', max_length=20)
    presidenst = models.CharField('Президент', max_length=20)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
