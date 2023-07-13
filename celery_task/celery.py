import logging
import os

from celery import Celery
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('celery_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

logger = logging.getLogger(__name__)


@shared_task
def send_email_reminder(email, reminder_text):
    logger.info(f"Reminder: {reminder_text}, Sent to: {email}")
