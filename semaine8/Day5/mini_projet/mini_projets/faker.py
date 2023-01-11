from django.core.management.base import BaseCommand
from faker import Faker

from .models import Client

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        for i in range(100):
            client = Client(name=fake.name())
            client.save()

