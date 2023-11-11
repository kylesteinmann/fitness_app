from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    incremental_weight = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name
