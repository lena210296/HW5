from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
        widgets = {
            'rating': forms.NumberInput(attrs={'step': '0.01'}),
            'pubdate': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.rating is not None:
            self.initial['rating'] = f"{self.instance.rating:.2f}"
        self.fields['pubdate'].widget = forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
