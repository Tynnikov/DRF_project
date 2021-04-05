import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create random user.'

    def handle(self, *args, **kwargs):
        response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username': 'test0@mail.com', 'password': '123'})

        print(response.status_code)  # {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
        print(response.json())  # {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
