import json
from json import loads
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import UserForm, MuscleGroupForm, ExerciseForm, WorkoutForm
from .models import User, MuscleGroup, Exercise, Workout


def J(data, status=200):
    return HttpResponse(json.dumps(data, ensure_ascii=False, default=str),
                        content_type='application/json', status=status)


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request):
        return J(list(User.objects.values('id', 'username', 'email')))

    def post(self, request):
        f = UserForm(loads(request.body))
        return J({'id': f.save().pk}) if f.is_valid() else J({'error': f.errors}, 400)


@method_decorator(csrf_exempt, name='dispatch')
class MuscleGroupView(View):
    def get(self, request):
        return J(list(MuscleGroup.objects.values('id', 'name')))

    def post(self, request):
        f = MuscleGroupForm(loads(request.body))
        return J({'id': f.save().pk}) if f.is_valid() else J({'error': f.errors}, 400)


@method_decorator(csrf_exempt, name='dispatch')
class ExerciseView(View):
    def get(self, request):
        return J(list(Exercise.objects.values('id', 'name', 'muscle_group__name')))

    def post(self, request):
        f = ExerciseForm(loads(request.body))
        return J({'id': f.save().pk}) if f.is_valid() else J({'error': f.errors}, 400)


@method_decorator(csrf_exempt, name='dispatch')
class WorkoutView(View):
    def get(self, request):
        return J(list(Workout.objects.values('id', 'user__username', 'workout_date')))

    def post(self, request):
        f = WorkoutForm(loads(request.body))
        return J({'id': f.save().pk}) if f.is_valid() else J({'error': f.errors}, 400)