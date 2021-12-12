from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = 'Remove an API Key using the client name'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str,
                            help='Indicates the name of the client for the API key')

    def handle(self, *args, **kwargs):
        client = kwargs['client']
        api_key = APIKey.objects.get(name=client)
        api_key.delete()
        self.stdout.write(
            "Successfully deleted api key for the client %s" % client)
