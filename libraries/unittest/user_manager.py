import requests


def get_user(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if response.status_code != 200:
        raise Exception("Failed to get a user.")
    return response.json()


def create_user(user):
    response = requests.post(f"https://jsonplaceholder.typicode.com/users", data=user)
    if response.status_code != 201:
        raise Exception("Failed to create a user.")
    return response.json()

