# Generated by Django 4.0.2 on 2022-07-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_correct_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='correct_answer',
        ),
    ]
