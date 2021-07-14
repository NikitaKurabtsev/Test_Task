import requests

from account.models import User


# def save_user(username, first_name, last_name, gender, password, **kwargs):
#     user, is_create = User.objects.get_or_create(
#         username=username,
#         first_name=first_name,
#         last_name=last_name,
#         gender=gender,
#     )
#     if is_create:
#         user.password = password
#         user.save()
#
#     return user
#
#
# def import_randomuser(count=100):
#
#     url = f"https://randomuser.me/api/?results={count}"
#
#     data = requests.get(url).json()["results"]
#     for user_data in data:
#         save_user(
#             username=user_data.get("login", {}).get("username", ""),
#             first_name=user_data.get("name", {}).get("first", ""),
#             last_name=user_data.get("name", {}).get("last", ""),
#             gender=user_data.get("gender", ""),
#             password=user_data.get("login", {}).get("password", "")
#         )
#
#
# def import_service2():
#
#     data = []
#     for user_data in data:
#         save_user(**user_data)


class UserImportService:

    def save_user(self, username, first_name, last_name, gender, password, **kwargs):
        user, is_create = User.objects.get_or_create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        if is_create:
            user.password = password
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
