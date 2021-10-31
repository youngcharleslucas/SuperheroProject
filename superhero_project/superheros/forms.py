from django import forms
from django.forms import ModelForm, fields
from .models import Superhero

class HeroForm(ModelForm):
    class Meta:
        model = Superhero
        fields = ('name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase')
