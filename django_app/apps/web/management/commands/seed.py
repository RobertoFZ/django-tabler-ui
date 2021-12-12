from django.core.management.base import BaseCommand
from django_app.apps.web.services.seeds.seed_manager import SeedManager
import time


class Command(BaseCommand):
    help = 'Seed the database with basic data'

    def handle(self, *args, **kwargs):
        start = time.time()
        seed_manager = SeedManager()
        seed_manager.create()
        end = time.time()
        self.stdout.write(
            f"Database seeds run successfully, it took {round(end - start, 2)} seconds")
