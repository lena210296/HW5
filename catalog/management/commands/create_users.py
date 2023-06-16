from django.contrib.auth.models import User
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from faker import Faker


class Command(BaseCommand):
    command_help = 'Generates random users'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        fake = Faker()

        if num < 1 or num > 10:
            raise CommandError('Number of users must be between 1 and 10.')

        users_to_create = []

        for i in range(num):
            username = fake.name()
            email = username.replace(" ", "").lower() + "@domain.com"
            password = get_random_string(length=11)

            user = User(username=username, email=email, password=password)
            users_to_create.append(user)

        User.objects.bulk_create(users_to_create)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {num} users.'))
