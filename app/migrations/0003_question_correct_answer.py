# Generated by Django 4.0.2 on 2022-07-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_choice_choice_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.BooleanField(default=False),
        ),
    ]
