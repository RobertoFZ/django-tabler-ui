from django.core.management.base import BaseCommand
from django_app.apps.web.models import User

class Command(BaseCommand):
    help = 'Remove a User with the email indicated'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str,
                            help='Indicates the email of the user to remove')

    def handle(self, *args, **kwargs):
        email = kwargs['email']

        user = User.objects.get(email=email)
        user.delete()

        self.stdout.write("User %s deleted successfully" % (email))
