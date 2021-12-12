from pathlib import Path
import os
from django_app.apps.web.models.user import User


class ResetManager:
    def __init__(self):
        self.__assing_csv_path()

    def delete_all(self):
        self.__delete_users()

    def __assing_csv_path(self):
        file_path = Path(__file__).resolve().parent
        self.csv_base_folder_path = os.path.join(file_path, '../../seeds')

    def __delete_users(self):
        User.objects.all().delete()
