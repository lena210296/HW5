from django import forms


class TriangleForm(forms.Form):
    cathetus1 = forms.FloatField(label='Cathetus 1')
    cathetus2 = forms.FloatField(label='Cathetus 2')
