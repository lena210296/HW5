from django.contrib import messages
from django.shortcuts import render

from .celery import send_email_reminder
from .forms import ReminderForm


def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            reminder_text = form.cleaned_data['reminder_text']
            reminder_date = form.cleaned_data['reminder_date']

            send_email_reminder.apply_async(args=[email, reminder_text], eta=reminder_date)
            messages.success(request, 'Reminder scheduled successfully!')
    else:
        form = ReminderForm()

    return render(request, 'create_reminder.html', {'form': form})
