# Generated by Django 4.1.1 on 2022-09-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0008_animal_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]