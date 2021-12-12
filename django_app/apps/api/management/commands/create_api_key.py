from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = 'Create a new API Key for a client'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str,
                            help='Indicates the name of the client for the API key')

    def handle(self, *args, **kwargs):
        client = kwargs['client']
        client_name, key = APIKey.objects.create_key(name=client)
        self.stdout.write("Client: %s\n API Key: %s" % (client_name, key))
