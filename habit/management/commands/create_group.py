from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Создает группу "moderator".'

    def handle(self, *args, **kwargs):
        # Создаем группу "moderator"
        moderator_group, created = Group.objects.get_or_create(name="moderator")

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "moderator" создана.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "moderator" уже существует.'))
