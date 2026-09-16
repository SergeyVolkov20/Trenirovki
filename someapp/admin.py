from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MuscleGroup, Exercise, Workout, WorkoutExercise


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')


admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)