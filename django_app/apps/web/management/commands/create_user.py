from django.core.management.base import BaseCommand
from django_app.apps.web.models import User, UserRoles
import json


class Command(BaseCommand):
    help = 'Create a new User with the rol indicated'
    valid_roles = [UserRoles.ADMIN, UserRoles.USER]

    def add_arguments(self, parser):
        parser.add_argument('role', type=str,
                            help='Indicates the role of the user to create (admin, user)')
        parser.add_argument('email', type=str,
                            help='Indicates the email of the user to create')
        parser.add_argument('password', type=str,
                            help='Indicates the password of the user to create')

    def handle(self, *args, **kwargs):
        role = kwargs['role']
        email = kwargs['email']
        password = kwargs['password']
        self.stdout.write(json.dumps(kwargs))
        if not role in self.valid_roles:
            raise Exception('Invalid role.')

        user = User.objects.create(role=role, email=email)
        user.set_password(password)
        if role == UserRoles.ADMIN:
            user.is_staff = True
            user.is_superuser = True
        user.save()

        self.stdout.write("User created successfully with email %s and password %s" % (
            user.email, password))
