from django.core.management.base import BaseCommand
from profiles.models import UserInformation
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'remove added entries from Rating model'

    def handle(self, *args, **options):
        User.objects.filter(is_staff=0).delete()