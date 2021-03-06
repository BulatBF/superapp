# Generated by Django 3.1.7 on 2021-03-13 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название вопроса')),
                ('publication_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('question_text', models.TextField(verbose_name='Текст вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chois_text', models.CharField(max_length=64, verbose_name='Текст ответа')),
                ('votes', models.IntegerField(default=0, verbose_name='Всего ответов')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Вопрос')),
            ],
        ),
    ]
