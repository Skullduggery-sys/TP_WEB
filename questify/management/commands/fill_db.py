from django.core.management import BaseCommand
from questify.models import User, Author, Question, Answers, Tags
from faker import Faker


class Command(BaseCommand):
    help = 'fill database with test data'

    def handle(self, *args, **options):
        ratio = options['ratio']
        faker = Faker()

        for i in range(ratio):
            user = User.objects.create_user(faker.user_name(), faker.email(), faker.password())
            Author.objects.create(default_user=user)

        for i in range(ratio * 10):


