import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class QuestionManager(models.Manager):
    def new_question(self):
        return self.order_by('-creation_date')

    def best_question(self):
        return self.annotate(total_likes=Sum('questionslikes__value')).filter(total_likes__gt=80)


class Question(models.Model):
    author_ID = models.ForeignKey("Author", on_delete=models.PROTECT)
    text = models.TextField()
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField("Tags")
    creation_date = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    name = models.CharField(max_length=255)


class QuestionsLikes(models.Model):
    class MyEnum(models.IntegerChoices):
        VALUE_MINUS_ONE = -1
        VALUE_ZERO = 0
        VALUE_ONE = 1

    value = models.IntegerChoices(MyEnum.VALUE_ZERO, MyEnum.choices)
    sender = models.ForeignKey("Author", on_delete=models.PROTECT)
    question_ID = models.ForeignKey("Question", on_delete=models.PROTECT)


class AnswersLikes(models.Model):
    class MyEnum(models.IntegerChoices):
        VALUE_MINUS_ONE = -1
        VALUE_ZERO = 0
        VALUE_ONE = 1

    value = models.IntegerChoices(MyEnum.VALUE_ZERO, MyEnum.choices)
    sender = models.ForeignKey("Author", on_delete=models.PROTECT)
    answer_ID = models.ForeignKey("Answer", on_delete=models.PROTECT)


class Answers(models.Model):
    author_ID = models.ForeignKey("Author", on_delete=models.PROTECT)
    question_ID = models.ForeignKey("Question", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)


class Author(models.Model):
    birth_date = models.DateField(blank=True, null=True)
    default_user_ID = models.ForeignKey(User, on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to="./static/avatars/", blank=True, null=True)
