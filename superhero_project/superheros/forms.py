from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Superhero

class HeroForm(ModelForm):
    class Meta:
        model = Superhero
        fields = ('name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'alter_ego':forms.TextInput(attrs={'class': 'form-control'}),
            'primary_ability':forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_ability':forms.TextInput(attrs={'class': 'form-control'}),
            'catch_phrase':forms.TextInput(attrs={'class': 'form-control'}),
        }