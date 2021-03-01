from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from user.models import User


class Command(BaseCommand):
    help = 'Create random user.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(nick_name=get_random_string(), email=f'test{i}@mail.com', password='123', first_name=get_random_string(), last_name=get_random_string())
