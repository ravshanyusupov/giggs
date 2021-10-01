from django.shortcuts import render
# from django.views.generic.list import ListView
# Create your views here.
from .models import Car, Sort


def home(request):
    a = Car.objects.all()
    context = {
        'a': a
    }
    return render(request, 'base.html', context=context)
