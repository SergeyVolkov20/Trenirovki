from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class MuscleGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(
        MuscleGroup, on_delete=models.CASCADE, related_name='exercises'
    )


class Workout(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='workouts'
    )
    workout_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name='workout_exercises'
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE
    )
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)