from django import forms
from .models import Person


class TriangleForm(forms.Form):
    cathetus1 = forms.FloatField(label='Cathetus 1')
    cathetus2 = forms.FloatField(label='Cathetus 2')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']




