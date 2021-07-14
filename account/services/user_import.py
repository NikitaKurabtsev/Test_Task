import requests

from account.models import User

url = "https://randomuser.me/api/?results=100"

data = requests.get(url).json()["results"]

for user_data in data:

    user = User.objects.get_or_create(

        username=user_data.get("login", {}).get("username", ""),

        password=user_data.get("login", {}).get("password", ""),

        first_name=user_data.get("name", {}).get("first", ""),

        last_name=user_data.get("name", {}).get("last", ""),

        gender=user_data.get("gender", ""),

    )
