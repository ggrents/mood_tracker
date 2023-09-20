from django.test import TestCase



import requests

response = requests.post("http://127.0.0.1:8000/api/users/login", data={

    "username": "ggg",
    "password": "2996"
})
print(response.status_code)
print(response.text)
