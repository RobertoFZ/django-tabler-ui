from pathlib import Path
import os
from django_app.apps.web.models.user import User, UserRoles
from django_app.apps.web.services.seeds.reset_manager import ResetManager


class SeedManager:
    __users = [{
        'email': 'admin@django.com',
        'role': UserRoles.ADMIN,
    }, {
        'email': 'user@django.com',
        'role': UserRoles.USER,
    }]

    def __init__(self):
        self.__assing_csv_path()

    def create(self):
        self.__delete_all()
        self.__create_users()

    def __assing_csv_path(self):
        file_path = Path(__file__).resolve().parent
        self.csv_base_folder_path = os.path.join(file_path, '../../seeds')

    def __delete_all(self):
        manager = ResetManager()
        manager.delete_all()

    def __create_users(self):
        for _user in self.__users:
            user = User(
                email=_user['email'],
                role=_user['role'],
            )
            user.set_password('django')
            user.save()
