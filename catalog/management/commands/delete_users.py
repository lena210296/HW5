from django.contrib.auth.models import User
from django.core.management import CommandError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    command_help = 'Deletes users by ID'

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int, help='Specify the user IDs to be deleted')

    def handle(self, *args, **kwargs):
        user_ids = kwargs['user_ids']

        superuser_ids = list(User.objects.filter(is_superuser=True).values_list('id', flat=True))

        superuser_id_intersection = set(user_ids) & set(superuser_ids)
        if superuser_id_intersection:
            raise CommandError(
                f"Cannot delete superuser(s) with ID(s): {', '.join(str(uid) for uid in superuser_id_intersection)}")

        existing_user_ids = list(User.objects.values_list('id', flat=True))

        non_existing_ids = set(user_ids) - set(existing_user_ids)
        if non_existing_ids:
            raise CommandError(f"User(s) with ID(s) {', '.join(str(uid) for uid in non_existing_ids)} do(es) not exist")

        User.objects.filter(id__in=user_ids).delete()

        self.stdout.write(self.style.SUCCESS(f"Successfully deleted {len(user_ids)} user(s)."))
