from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('muscle-groups/', views.MuscleGroupView.as_view()),
    path('exercises/', views.ExerciseView.as_view()),
    path('workouts/', views.WorkoutView.as_view()),
]