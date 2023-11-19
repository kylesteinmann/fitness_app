from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    incremental_weight = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name
 
class Routine(models.Model):
    name = models.CharField(max_length=200)
    exercises = models.ManyToManyField('Exercise', through='RoutineExercise', blank=True)    
    
    def __str__(self):
        return self.name

class RoutineExercise(models.Model):
    routine = models.ForeignKey('Routine', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    repetitions = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f"{self.exercise.name} in {self.routine.name}"

