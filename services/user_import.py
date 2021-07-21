import requests

from account.models import User


class UserImportService:

    def save_user(self, username, first_name, last_name, gender, password, **kwargs):
        user, is_create = User.objects.get_or_create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        if is_create:
            user.set_password(password)
            user.save()

        return user

    def import_randomuser(self, count=100):

        url = f"https://randomuser.me/api/?results={count}"

        data = requests.get(url).json()["results"]
        for user_data in data:
            self.save_user(
                username=user_data.get("login", {}).get("username", ""),
                first_name=user_data.get("name", {}).get("first", ""),
                last_name=user_data.get("name", {}).get("last", ""),
                gender=user_data.get("gender", ""),
                password=user_data.get("login", {}).get("password", "")
            )

    def create_single_user(self):
        user, is_create = User.objects.get_or_create(
            username="newuser",
            first_name="Alex",
            last_name="Woods"
        )
        if is_create:
            user.set_password('12345')
            user.save()

        return user
