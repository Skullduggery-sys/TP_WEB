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

            Tags.objects.create(name=f'Tag#{ratio}')

        for i in range(ratio * 10):
            random_author = Author.objects.order_by('?').first()
            random_tags = Tags.objects.order_by('?')[:3]
            question = Question.objects.create(text=faker.text(), title=faker.company(), author=random_author)
            question.tags.set(random_tags)

        for i in range(ratio * 100):



