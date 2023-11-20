# Generated by Django 4.2.7 on 2023-11-20 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='./static/avatars/')),
                ('default_user_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.author')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(-1, 'dislike'), (0, 'indifferent'), (1, 'like')], default=0)),
                ('question_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.question')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.author')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='questify.tags'),
        ),
        migrations.CreateModel(
            name='AnswersLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(-1, 'dislike'), (0, 'indifferent'), (1, 'like')], default=0)),
                ('answer_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.answers')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.author')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='author_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questify.author'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questify.question'),
        ),
    ]
