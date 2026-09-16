from django import forms
from .models import User, MuscleGroup, Exercise, Workout

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class MuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['user', 'workout_date', 'start_time', 'end_time', 'duration_minutes']