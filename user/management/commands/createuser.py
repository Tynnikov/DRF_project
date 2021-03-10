from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from loguru import logger
from user.models import User

logger.add("log/command.log", format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}", level="DEBUG", rotation="1MB", compression="zip", backtrace=True, diagnose=True,
           filter=lambda record: record["extra"].get("name") == "command")
logger_command = logger.bind(name='command')

class Command(BaseCommand):
    help = 'Create random user.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        logger_command.debug(f'Start management command')
        total = kwargs['total']
        for i in range(total):
            u = User.objects.create_user(nick_name=get_random_string(), email=f'test_command{i}@mail.com', password='123', first_name=get_random_string(), last_name=get_random_string())
            logger_command.debug(f'Create user {u}')
