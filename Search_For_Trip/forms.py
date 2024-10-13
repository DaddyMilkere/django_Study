from django import forms
from select import select

from .models import City
class CityForm(forms.ModelForm):
    class Meta:
        model= City
        fields= '__all__'
        labels= {
            'name' :'Название города',
            'country': 'Страна, где находится город'
        }
