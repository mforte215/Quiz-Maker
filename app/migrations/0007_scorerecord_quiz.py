# Generated by Django 4.0.2 on 2022-08-03 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_scorerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorerecord',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scorerecords', to='app.quiz'),
        ),
    ]
