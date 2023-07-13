from django import forms
from django.utils import timezone


class ReminderForm(forms.Form):
    email = forms.EmailField()
    reminder_text = forms.CharField(widget=forms.Textarea)
    reminder_date = forms.DateTimeField(initial=timezone.now, help_text='Format: YYYY-MM-DD HH:MM:SS')

    def clean_reminder_date(self):
        reminder_date = self.cleaned_data['reminder_date']
        if reminder_date < timezone.now():
            raise forms.ValidationError("Reminder date cannot be in the past.")
        if reminder_date > timezone.now() + timezone.timedelta(days=2):
            raise forms.ValidationError("Reminder date cannot be more than two days from now.")
        return reminder_date
