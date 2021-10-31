from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Superhero
from .forms import HeroForm

# Create your views here.

def index(request):
    all_heros = Superhero.objects.all()
    context = {
        'all_heros' : all_heros
    }
    return render(request, 'superheros/index.html', context )

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheros/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego =request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheros:index'))

    else:
        return render(request, 'superheros/create.html')

def delete_hero(request, hero_id):
    deleted_hero=Superhero.objects.get(pk=hero_id)
    deleted_hero.delete()
    # why is delete not recognized in the intellitext? Save is recognized. It works though.
    return HttpResponseRedirect(reverse('superheros:index'))

def update_hero(request, hero_id):
    updated_hero=Superhero.objects.get(pk=hero_id)
    form = HeroForm(request.POST or None, instance = updated_hero) 
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'updated_hero': updated_hero
    }
    return render(request, 'superheros/update_hero.html', context)
    # return HttpResponseRedirect(reverse('superheros:index')), context

    # def update_hero(request, hero_id):
#     update_hero=Superhero.objects.get(pk=hero_id)
#     context = {
#         'update_hero': update_hero
      
#     }
#     return render(request, 'superheros/update_hero.html', context)

# def update_hero(request, hero_id):
#     update_hero=Superhero.objects.get(pk=hero_id)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         alter_ego =request.POST.get('alter_ego')
#         primary = request.POST.get('primary')
#         secondary = request.POST.get('secondary')
#         catchphrase = request.POST.get('catchphrase')
#         new_hero = update_hero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
#         new_hero.save()
#         return HttpResponseRedirect(reverse('superheros:index'))

# def update_hero(request, hero_id):
#     submitted = False
#     if request.method == "POST":
#         form = HeroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect(reverse('superheros:index')), submitted = True
#             return HttpResponseRedirect(reverse('superheros:index'))
#     else:
#         form = HeroForm
#         if 'submitted' in request.GET:
#             submitted = True
#     context = {
#         'form': form,
#         'submitted': submitted
#     }
#     return render(request, 'superheros/update_hero.html', context)

# def update_hero(request, hero_id):
#     form = HeroForm(request.POST) 
#     context = {
#         'form': form,
#     }
#     return render(request, 'superheros/update_hero.html', context)
