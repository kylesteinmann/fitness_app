from django.db import models

# Create your models here.


class Routine(models.Model):
    name = models.CharField(max_length=200)
    exercises = models.ManyToManyField('exercises.Exercise', blank=True)

    def __str__(self):
        return self.name
